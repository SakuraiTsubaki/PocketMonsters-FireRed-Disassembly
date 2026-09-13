#!/usr/bin/env python3
"""Validate the audited AgbMain extent for one FireRed baseline.

This deliberately avoids an external disassembler dependency.  ARMv4T Thumb BL
instructions are recognized as the standard two-halfword F000/F800 pair, which
is sufficient to reproduce the call-count invariant recorded during the ROM
audit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROM_BASE = 0x08000000
AGB_MAIN_START = 0x080003A4


def u16le(data: bytes, offset: int) -> int:
    return data[offset] | (data[offset + 1] << 8)


def count_thumb_bl(data: bytes) -> int:
    count = 0
    i = 0
    while i + 3 < len(data):
        first = u16le(data, i)
        second = u16le(data, i + 2)
        if (first & 0xF800) == 0xF000 and (second & 0xF800) == 0xF800:
            count += 1
            i += 4
        else:
            i += 2
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("rom", type=Path)
    parser.add_argument("target", choices=(
        "jp_rev0", "jp_rev1", "us_rev0", "us_rev1",
        "fr", "de", "it", "es",
    ))
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("analysis/agb_main/variants.json"),
    )
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    expected = manifest["baselines"][args.target]

    rom = args.rom.read_bytes()
    if len(rom) != 16 * 1024 * 1024:
        raise SystemExit(f"unexpected ROM size: {len(rom)}")

    start = AGB_MAIN_START - ROM_BASE
    end_address = int(expected["end_exclusive"], 16)
    end = end_address - ROM_BASE
    body = rom[start:end]

    observed_calls = count_thumb_bl(body)
    expected_calls = int(expected["thumb_bl_calls"])
    expected_size = int(expected["size"])

    result = {
        "target": args.target,
        "start": f"0x{AGB_MAIN_START:08X}",
        "end_exclusive": f"0x{end_address:08X}",
        "size": len(body),
        "sha256": hashlib.sha256(body).hexdigest(),
        "thumb_bl_calls": observed_calls,
        "print_init_call": bool(expected["print_init_call"]),
        "flash_memory_guard": bool(expected["flash_memory_guard"]),
        "size_matches": len(body) == expected_size,
        "bl_count_matches": observed_calls == expected_calls,
    }
    print(json.dumps(result, indent=2))

    return 0 if result["size_matches"] and result["bl_count_matches"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

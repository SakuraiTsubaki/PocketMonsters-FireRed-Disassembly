#!/usr/bin/env python3
"""Classify byte differences between same-size FireRed code objects.

Differences are assigned to one of three buckets:
  * address_literal_bytes: bytes belonging to aligned 32-bit GBA pointers
  * thumb_bl_bytes: bytes belonging to ARMv4T Thumb BL instruction pairs
  * other_bytes: differences not explained by either relocation class

This is the classifier used by the cross-version object audit tables.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def plausible_gba_address(value: int) -> bool:
    return ((value >> 24) & 0xFF) in {0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09}


def address_literal_byte(data: bytes, index: int) -> bool:
    start = index & ~3
    if start + 4 > len(data):
        return False
    return plausible_gba_address(int.from_bytes(data[start:start + 4], "little"))


def thumb_bl_byte(data: bytes, index: int) -> bool:
    halfword_start = index & ~1
    for start in (halfword_start, halfword_start - 2):
        if start < 0 or start + 4 > len(data):
            continue
        first = int.from_bytes(data[start:start + 2], "little")
        second = int.from_bytes(data[start + 2:start + 4], "little")
        if ((first & 0xF800) == 0xF000
                and (second & 0xF800) == 0xF800
                and start <= index < start + 4):
            return True
    return False


def parse_offset(value: str) -> int:
    return int(value, 0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("reference_rom", type=Path)
    parser.add_argument("target_rom", type=Path)
    parser.add_argument("reference_start", type=parse_offset)
    parser.add_argument("target_start", type=parse_offset)
    parser.add_argument("size", type=parse_offset)
    args = parser.parse_args()

    reference_rom = args.reference_rom.read_bytes()
    target_rom = args.target_rom.read_bytes()
    ref = reference_rom[args.reference_start:args.reference_start + args.size]
    target = target_rom[args.target_start:args.target_start + args.size]

    if len(ref) != args.size or len(target) != args.size:
        raise SystemExit("requested object extends beyond a ROM")

    differing = [i for i, (a, b) in enumerate(zip(ref, target)) if a != b]
    address = 0
    branch = 0
    other = 0

    for index in differing:
        if address_literal_byte(ref, index) or address_literal_byte(target, index):
            address += 1
        elif thumb_bl_byte(ref, index) or thumb_bl_byte(target, index):
            branch += 1
        else:
            other += 1

    result = {
        "size": args.size,
        "byte_differences": len(differing),
        "address_literal_bytes": address,
        "thumb_bl_bytes": branch,
        "other_bytes": other,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

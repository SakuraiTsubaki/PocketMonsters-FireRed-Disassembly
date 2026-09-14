#!/usr/bin/env python3
"""Extract FireRed Pokémon battle sprites into disassembly-ready source paths.

ROM binaries are input-only and are never copied. Multiple language/revision ROMs are
compared byte-for-byte; identical assets are emitted once and source equivalence is
recorded in a manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path
from typing import Dict, List, Tuple

from PIL import Image

ROM_BASE = 0x08000000
SPECIES = {
    1: "bulbasaur", 2: "ivysaur", 3: "venusaur", 4: "charmander", 5: "charmeleon",
    6: "charizard", 7: "squirtle", 8: "wartortle", 9: "blastoise", 10: "caterpie",
    11: "metapod", 12: "butterfree", 13: "weedle", 14: "kakuna", 15: "beedrill",
    16: "pidgey", 17: "pidgeotto", 18: "pidgeot", 19: "rattata", 20: "raticate",
    21: "spearow", 22: "fearow", 23: "ekans", 24: "arbok", 25: "pikachu",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def pointer_to_offset(pointer: int, rom_size: int) -> int | None:
    return pointer - ROM_BASE if ROM_BASE <= pointer < ROM_BASE + rom_size else None


def lz_size(rom: bytes, offset: int | None) -> int | None:
    if offset is None or offset < 0 or offset + 4 > len(rom) or rom[offset] != 0x10:
        return None
    return rom[offset + 1] | (rom[offset + 2] << 8) | (rom[offset + 3] << 16)


def lz77_decompress(rom: bytes, offset: int) -> bytes:
    if rom[offset] != 0x10:
        raise ValueError(f"not GBA LZ77 at 0x{offset:X}")
    size = rom[offset + 1] | (rom[offset + 2] << 8) | (rom[offset + 3] << 16)
    src = offset + 4
    out = bytearray()
    while len(out) < size:
        flags = rom[src]
        src += 1
        for bit in range(7, -1, -1):
            if len(out) >= size:
                break
            if flags & (1 << bit):
                a, b = rom[src], rom[src + 1]
                src += 2
                length = (a >> 4) + 3
                displacement = (((a & 0x0F) << 8) | b) + 1
                for _ in range(length):
                    out.append(out[-displacement])
            else:
                out.append(rom[src])
                src += 1
    return bytes(out[:size])


def find_sprite_tables(rom: bytes, probe: int = 12) -> List[int]:
    result: List[int] = []
    n = len(rom)
    for off in range(0, n - 8 * probe, 4):
        ptr, size, tag = struct.unpack_from("<IHH", rom, off)
        if size != 0x800 or tag != 0 or lz_size(rom, pointer_to_offset(ptr, n)) != 0x800:
            continue
        for i in range(1, probe):
            ptr, size, tag = struct.unpack_from("<IHH", rom, off + i * 8)
            if size != 0x800 or tag != i or lz_size(rom, pointer_to_offset(ptr, n)) != 0x800:
                break
        else:
            result.append(off)
    return result


def find_palette_table(rom: bytes, start_tag: int, probe: int = 12) -> int:
    n = len(rom)
    for off in range(0, n - 8 * probe, 4):
        ptr, tag, _ = struct.unpack_from("<IHH", rom, off)
        if tag != start_tag or lz_size(rom, pointer_to_offset(ptr, n)) != 32:
            continue
        for i in range(1, probe):
            ptr, tag, _ = struct.unpack_from("<IHH", rom, off + i * 8)
            if tag != start_tag + i or lz_size(rom, pointer_to_offset(ptr, n)) != 32:
                break
        else:
            return off
    raise RuntimeError(f"palette table tag {start_tag} not found")


def get_sheet(rom: bytes, table: int, species: int) -> bytes:
    ptr, size, tag = struct.unpack_from("<IHH", rom, table + species * 8)
    if size != 0x800 or tag != species:
        raise RuntimeError(f"unexpected sprite entry for species {species}")
    return lz77_decompress(rom, ptr - ROM_BASE)


def get_palette(rom: bytes, table: int, species: int) -> bytes:
    ptr, _tag, _pad = struct.unpack_from("<IHH", rom, table + species * 8)
    return lz77_decompress(rom, ptr - ROM_BASE)


def palette_rgb(raw: bytes) -> List[Tuple[int, int, int]]:
    colors = []
    for i in range(16):
        value = struct.unpack_from("<H", raw, i * 2)[0]
        colors.append(((value & 31) * 255 // 31,
                       ((value >> 5) & 31) * 255 // 31,
                       ((value >> 10) & 31) * 255 // 31))
    return colors


def jasc_palette(raw: bytes) -> str:
    lines = ["JASC-PAL", "0100", "16"]
    lines.extend(f"{r} {g} {b}" for r, g, b in palette_rgb(raw))
    return "\n".join(lines) + "\n"


def render_indexed(sheet: bytes, palette: bytes) -> Image.Image:
    image = Image.new("P", (64, 64))
    flat = [channel for rgb in palette_rgb(palette) for channel in rgb]
    image.putpalette(flat + [0] * (768 - len(flat)))
    pixels = image.load()
    for tile_y in range(8):
        for tile_x in range(8):
            base = (tile_y * 8 + tile_x) * 32
            for y in range(8):
                for x in range(8):
                    packed = sheet[base + y * 4 + x // 2]
                    pixels[tile_x * 8 + x, tile_y * 8 + y] = packed & 0x0F if x % 2 == 0 else packed >> 4
    return image


def detect(rom: bytes) -> Dict[str, int]:
    sheets = find_sprite_tables(rom)
    if len(sheets) < 2:
        raise RuntimeError("front/back sprite tables not found")
    return {
        "front": sheets[0],
        "back": sheets[1],
        "normal_palette": find_palette_table(rom, 0),
        "shiny_palette": find_palette_table(rom, 500),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("roms", nargs="+", type=Path)
    ap.add_argument("--output", type=Path, required=True,
                    help="disassembly graphics/pokemon directory")
    ap.add_argument("--manifest", type=Path,
                    help="optional manifest path; defaults under OUTPUT/manifests")
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=25)
    args = ap.parse_args()

    loaded = []
    sources = []
    for path in args.roms:
        rom = path.read_bytes()
        tables = detect(rom)
        loaded.append((path, rom, tables))
        sources.append({
            "file": path.name,
            "sha1": hashlib.sha1(rom).hexdigest(),
            "game_code": rom[0xAC:0xB0].decode("ascii", "replace"),
            "revision": rom[0xBC],
            "tables": {k: f"0x{v:X}" for k, v in tables.items()},
        })

    args.output.mkdir(parents=True, exist_ok=True)
    manifest = {"sources": sources, "species": []}

    for species in range(args.start, args.end + 1):
        name = SPECIES.get(species, f"species_{species:03d}")
        variants = []
        for path, rom, tables in loaded:
            parts = {
                "front": get_sheet(rom, tables["front"], species),
                "back": get_sheet(rom, tables["back"], species),
                "normal_palette": get_palette(rom, tables["normal_palette"], species),
                "shiny_palette": get_palette(rom, tables["shiny_palette"], species),
            }
            variants.append((path.name, parts))

        canonical = variants[0][1]
        for source, parts in variants[1:]:
            for key, value in canonical.items():
                if value != parts[key]:
                    raise RuntimeError(f"{species:03d} {name}: {key} differs in {source}")

        folder = args.output / name
        folder.mkdir(parents=True, exist_ok=True)
        for side in ("front", "back"):
            target = folder / f"{side}.png"
            render_indexed(canonical[side], canonical["normal_palette"]).save(target, optimize=True, bits=4)
        (folder / "normal.pal").write_text(jasc_palette(canonical["normal_palette"]), encoding="ascii")
        (folder / "shiny.pal").write_text(jasc_palette(canonical["shiny_palette"]), encoding="ascii")

        manifest["species"].append({
            "national_dex": species,
            "name": name,
            "canonical_source": variants[0][0],
            "shared_by": [source for source, _ in variants],
            "raw_hashes": {key: sha256(value) for key, value in canonical.items()},
            "paths": {
                "front": f"graphics/pokemon/{name}/front.png",
                "back": f"graphics/pokemon/{name}/back.png",
                "normal_palette": f"graphics/pokemon/{name}/normal.pal",
                "shiny_palette": f"graphics/pokemon/{name}/shiny.pal",
            },
        })

    manifest_path = args.manifest or args.output / "manifests" / f"battle_{args.start:03d}_{args.end:03d}.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

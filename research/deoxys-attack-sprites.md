# Japanese Deoxys Attack Forme sprites

Target: BPRJ rev0, SHA-256 `1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486`.

The two previously neutral Japanese version sprite sheets are now identified from the ROM's `CompressedSpriteSheet` entries. Both entries have tag `0x019A`, which is species 410 (`SPECIES_DEOXYS`), and size `0x0800`. The front entry at `0x1F5360` belongs to the table beginning at `0x1F4690`; the back entry at `0x1F6800` belongs to the table beginning at `0x1F5B30`. Those derived bases have 28 and 9 decoded Thumb literal references respectively, so the entries are tied to runtime-consumed species tables rather than named only by visual inspection.

The palette entry is at `0x1F75C0`, points to the 16-color LZ77 stream at `0xD39D48`, and carries the same species tag. The published JASC palette and color PNGs are reconstructed from that verified ROM data. The PNG layout is ROM tile order (16×8 tiles, 2× display scale); it is an asset sheet, not an in-game composited screenshot.

The role and version form are cross-checked against pinned primary reconstruction source `pret/pokefirered@037335f4c725d7c9aecdac87066f2002b4bd7e14`: `front_pic_table.h` and `back_pic_table.h` index Deoxys in the corresponding tables, while `src/data/graphics/pokemon.h` selects `graphics/pokemon/deoxys/front.4bpp.lz` and `back.4bpp.lz` under `FIRERED`. `src/decompress.c` consumes the tables through `DecompressPicFromTable` / `LoadSpecialPokePic` and applies the Deoxys tile duplication path.

No compressed or decoded ROM binary is published. Reports retain ROM identity, source offsets, compressed/decoded hashes, table metadata, palette provenance, and output hashes.

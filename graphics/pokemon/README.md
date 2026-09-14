# Pokémon graphics

Pokémon assets in this directory are stored as FireRed disassembly source files.

## Source layout

Each species uses the canonical source-style path:

- `graphics/pokemon/<species>/front.png`
- `graphics/pokemon/<species>/back.png`
- `graphics/pokemon/<species>/normal.pal`
- `graphics/pokemon/<species>/shiny.pal`

The PNGs preserve the 4bpp palette-index order; shiny coloration is represented by `shiny.pal` rather than duplicate shiny PNGs.

## Deduplication

- ROM binaries are input-only and are never committed.
- Language/revision ROMs are compared before emission.
- Byte-identical sprite and palette assets are stored once in the shared disassembly tree.
- Version membership, ROM hashes, table offsets, and raw asset hashes are recorded in `manifests/` instead of duplicating identical graphics.

## Upload batches

Sprite assets are added in small National Dex batches. Do not mass-upload the full set in one commit.

`tools/sprites/extract_pokemon_battle_sprites.py` recreates this layout directly from the input ROMs.

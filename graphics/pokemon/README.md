# Pokémon battle sprites

This directory contains ROM-extracted Pokémon battle sprite assets for FireRed.

## Deduplication policy

- ROM binaries are input-only and are never committed.
- Identical sprite data shared by language/revision ROMs is stored only once.
- Source ROM membership, table offsets, and hashes are recorded in batch manifests.
- Normal and shiny renders are kept separately because their palettes differ visually.
- Uploads are intentionally split into small National Dex batches instead of one large asset dump.
- Exact duplicate rendered/data assets discovered later are represented by manifest aliases instead of duplicate files.

## Current extraction format

Each species directory may contain:

- `front.4bpp` / `back.4bpp` — decompressed 64×64 GBA 4bpp sprite data
- `normal.gbapal` / `shiny.gbapal` — decompressed 16-color BGR555 palettes
- `front.png` / `back.png` — normal-color review images
- `front_shiny.png` / `back_shiny.png` — shiny-color review images

See `tools/sprites/extract_pokemon_battle_sprites.py` for the reproducible extractor and `manifests/` for source/deduplication records.

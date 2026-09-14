# Sprite Asset Policy

This repository stores sprite assets in disassembly-ready source paths, not in a separate archival bucket.

## Layout

Pokémon battle sprites follow the canonical FireRed disassembly layout:

- `graphics/pokemon/<species>/front.png`
- `graphics/pokemon/<species>/back.png`
- `graphics/pokemon/<species>/normal.pal`
- `graphics/pokemon/<species>/shiny.pal`

Where raw intermediate data is needed for verification, it belongs under analysis or tooling outputs and is not the primary source layout.

## Batch uploads

Sprite work is committed in small batches. Do not mass-upload the whole sprite set in one commit.

## Deduplication

If multiple language/revision ROMs contain byte-identical sprite assets, store one canonical source asset only. Record per-version equivalence in manifests/analysis instead of duplicating identical files.

## ROM policy

ROM binaries are never committed. Reconstructed source assets, PNGs, palettes, source code, manifests, and verification data are allowed.

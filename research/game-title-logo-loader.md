# Localized game-title logo loader provenance

The English, German, French, Italian, and Spanish 8bpp title-logo streams were each traced through their complete retail ROM. Every stream has one stored pointer and one Thumb consumer that passes the asset in `r1` to the release-local `DecompressAndCopyTileDataToVram` routine. The other observed register arguments are zero, selecting background 0 with tile rather than tilemap transfer.

This connects every existing localized palette, compressed-range digest, decoded tile digest, and PNG to state 1 of `CB2_InitTitleScreen`. `pret/pokefirered` commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/title_screen.c`, corroborates the names and call semantics.

The Japanese title composition is not treated as though it used this localized logo asset. Its separate version-specific sprite sheets remain independently documented. No ROM bytes are published.

# FireRed localized European game-title logos

The English revision-0 asset establishes the title-logo layout: a 256-entry
GBA BGR555 palette immediately precedes a BIOS-LZ77 stream that expands to
256 8bpp tiles. The German, French, Italian, and Spanish retail ROMs preserve
that structure while providing localized logo pixels.

Each ROM is gated by its independently cataloged SHA-256. The common palette
extractor converts the 512-byte BGR555 palette to JASC-PAL, and the common
8bpp extractor renders the following streams:

| Language | Game code | Palette | Tiles |
| --- | --- | ---: | ---: |
| German | BPRD | `0xEA9FE0` | `0xEAA1E0` |
| French | BPRF | `0xEAA020` | `0xEAA220` |
| Italian | BPRI | `0xEA9FFC` | `0xEAA1FC` |
| Spanish | BPRS | `0xEAA058` | `0xEAA258` |

All reports and the consolidated manifest hash the source ranges, decoded
tiles, palettes, and PNGs. No raw ROM bytes or compressed streams are kept.

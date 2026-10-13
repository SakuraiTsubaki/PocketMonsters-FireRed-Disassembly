# Global version-specific 4bpp sprite sheets

The Japanese `BPRJ` release remains the origin reference. This result extends the same two version-specific sprite sheets to the official English, German, French, Italian, and Spanish revision-0 releases without treating those releases as interchangeable ROMs.

Each verified local ROM was scanned for valid BIOS-LZ77 streams that decode to 4,096 bytes. FireRed and LeafGreen each contain 54 such streams in the full ROM; 52 decoded hashes are shared between the games. The two remaining FireRed streams exactly match the two previously extracted Japanese FireRed sheets by compressed and decompressed SHA-256. That cross-version comparison establishes the asset correspondence without relying on filenames or visual similarity alone.

| Language | Release | Sheet 0 | Sheet 1 |
| --- | --- | ---: | ---: |
| English | BPRE rev 0 | `0xE3958C` | `0xE39D70` |
| German | BPRD rev 0 | `0xE39580` | `0xE39D64` |
| French | BPRF rev 0 | `0xE3958C` | `0xE39D70` |
| Italian | BPRI rev 0 | `0xE39584` | `0xE39D68` |
| Spanish | BPRS rev 0 | `0xE3958C` | `0xE39D70` |

Sheet 0 decodes to SHA-256 `ed6b7c3b3be626897d54ac922eee955f0616611cbe7eeafb416bf5e2623882e0`; sheet 1 decodes to `76478bca4bc91a53cee1c2704aa83877b6bca240a24dd127b11c8ba03a276225` in every language. The language-specific paths are retained so every published PNG has direct ROM provenance even though Git can deduplicate identical content.

Each output is 128 4bpp tiles rendered in ROM tile order as a 16×8 tile sheet and enlarged 2× to a 256×128 PNG. The deterministic grayscale index preview is intentional: the matching runtime palette has not yet been proven. Raw compressed or decoded ROM bytes are not stored.

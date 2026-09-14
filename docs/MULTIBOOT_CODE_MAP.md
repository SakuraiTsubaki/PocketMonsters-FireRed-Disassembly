# `multiboot.c` cross-version code map

`multiboot.c` begins at `MultiBootInit`. All eight audited FireRed baselines emit an object of the same size: `0x6B4` (1716 bytes).

| Baseline | Start | End exclusive |
|---|---:|---:|
| JP Rev 0 | `0x0800B600` | `0x0800BCB4` |
| JP Rev 1 | `0x0800B56C` | `0x0800BC20` |
| US Rev 0 | `0x0800BC20` | `0x0800C2D4` |
| US Rev 1 | `0x0800BC34` | `0x0800C2E8` |
| French | `0x0800BB8C` | `0x0800C240` |
| German | `0x0800BBA0` | `0x0800C254` |
| Italian | `0x0800BBA0` | `0x0800C254` |
| Spanish | `0x0800BB8C` | `0x0800C240` |

## Family behavior

Within the Japanese family and within the international family, all differences are explained by relocated address literals and Thumb `BL` destinations. `analysis/multiboot/object_audit.csv` records zero unexplained bytes within both families.

A direct Japanese-vs-international comparison, however, contains genuine non-relocation code differences even though the object lengths match. Therefore equal size must not be interpreted as byte-identical source output across localization families.

The current implementation policy is to preserve one logical multiboot source while allowing the verified localization family to affect emitted code where ROM analysis requires it. No separate per-language source copies should be introduced without evidence.

The next object begins at `CB2_MainMenu` in `main_menu.c`.

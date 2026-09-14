# `string_util.c` cross-version code map

`string_util.c` follows `sprite.c` in every audited FireRed baseline. Its object size is language-family dependent.

| Baseline | Start | End exclusive | Size |
|---|---:|---:|---:|
| JP Rev 0 | `0x08008870` | `0x08008EAC` | `0x63C` (1596) |
| JP Rev 1 | `0x080087DC` | `0x08008E18` | `0x63C` (1596) |
| US Rev 0 | `0x08008CF4` | `0x08009480` | `0x78C` (1932) |
| US Rev 1 | `0x08008D08` | `0x08009494` | `0x78C` (1932) |
| French | `0x08008C60` | `0x080093EC` | `0x78C` (1932) |
| German | `0x08008C74` | `0x08009400` | `0x78C` (1932) |
| Italian | `0x08008C74` | `0x08009400` | `0x78C` (1932) |
| Spanish | `0x08008C60` | `0x080093EC` | `0x78C` (1932) |

## Build families

The Japanese object is 336 bytes smaller than the international object. This is a real localization-family distinction, not accumulated linker drift.

Within each family, every observed byte difference is explained by relocated address literals or Thumb `BL` destinations. The audit records `other_bytes = 0` for every non-reference build. See `analysis/string_util/object_audit.csv`.

This supports one shared source implementation per localization family, selected through the verified Japanese text-engine configuration rather than eight independent source copies.

The next object begins with `IsWirelessAdapterConnected`, the first function of `link.c`.

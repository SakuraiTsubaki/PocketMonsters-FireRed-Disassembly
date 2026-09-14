# `link.c` cross-version code map

`link.c` begins with `IsWirelessAdapterConnected` and ends immediately before `MultiBootInit` from `multiboot.c`.

| Baseline | Start | End exclusive | Size |
|---|---:|---:|---:|
| JP Rev 0 | `0x08008EAC` | `0x0800B600` | `0x2754` (10068) |
| JP Rev 1 | `0x08008E18` | `0x0800B56C` | `0x2754` (10068) |
| US Rev 0 | `0x08009480` | `0x0800BC20` | `0x27A0` (10144) |
| US Rev 1 | `0x08009494` | `0x0800BC34` | `0x27A0` (10144) |
| French | `0x080093EC` | `0x0800BB8C` | `0x27A0` (10144) |
| German | `0x08009400` | `0x0800BBA0` | `0x27A0` (10144) |
| Italian | `0x08009400` | `0x0800BBA0` | `0x27A0` (10144) |
| Spanish | `0x080093EC` | `0x0800BB8C` | `0x27A0` (10144) |

## Localization split

The Japanese object is 76 bytes smaller than the international object. Public reconstructed source also contains localized/link-test paths whose emitted code can depend on build configuration, so this project treats the size difference as a real build-family property rather than address drift.

Within each family, the ROM audit finds only relocated pointer/literal bytes and Thumb `BL` destination bytes; `other_bytes` is zero for every non-reference member. See `analysis/link/object_audit.csv`.

Therefore the byte-exact implementation should keep one logical `link.c` source and use explicit verified localization/build predicates where required. It should not maintain eight regional forks.

The next object is `multiboot.c`, beginning at `MultiBootInit`.

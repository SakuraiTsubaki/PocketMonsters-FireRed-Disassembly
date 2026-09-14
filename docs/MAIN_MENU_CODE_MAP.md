# `main_menu.c` cross-version code map

`main_menu.c` begins at `CB2_MainMenu` and ends immediately before `HandleLinkBattleSetup` in `battle_controllers.c`.

| Baseline | Start | End exclusive | Size |
|---|---:|---:|---:|
| JP Rev 0 | `0x0800BCB4` | `0x0800CC54` | `0xFA0` (4000) |
| JP Rev 1 | `0x0800BC20` | `0x0800CBC0` | `0xFA0` (4000) |
| US Rev 0 | `0x0800C2D4` | `0x0800D230` | `0xF5C` (3932) |
| US Rev 1 | `0x0800C2E8` | `0x0800D244` | `0xF5C` (3932) |
| French | `0x0800C240` | `0x0800D1A0` | `0xF60` (3936) |
| German | `0x0800C254` | `0x0800D1B4` | `0xF60` (3936) |
| Italian | `0x0800C254` | `0x0800D1B4` | `0xF60` (3936) |
| Spanish | `0x0800C240` | `0x0800D1A0` | `0xF60` (3936) |

## Three emitted-size families

The audited retail ROMs form three emitted-size families: Japanese, US English, and European localization. Within JP and US families, all non-reference differences are relocation-only.

The European family has one verified localized immediate difference: French uses X coordinate `74` (`0x4A`) for the value column on the CONTINUE screen, while German, Italian and Spanish use `62` (`0x3E`) at the same four call sites. The four sites print the player name, play time, Pokédex count and badge count.

This matches the reconstructed `main_menu.c` layout: those values are the X coordinate passed to the text-printer calls in `PrintPlayerName`, `PrintPlayTime`, `PrintDexCount` and `PrintBadgeCount`.

This is intentional UI localization data, not linker drift. The byte-exact source must therefore preserve the French layout constant rather than forcing one international value.

Detailed counts are in `analysis/main_menu/object_audit.csv`.

The next object starts at `HandleLinkBattleSetup` in `battle_controllers.c`.

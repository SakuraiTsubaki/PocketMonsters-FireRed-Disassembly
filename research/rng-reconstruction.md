# FireRed Random and SeedRng

All eight catalogued FireRed releases were SHA-256 gated and searched independently. Every ROM contains exactly one standard RNG pair with `Random` hash `72526af8af03e60317e6ac115ece4a9415af188772c5432ec1c145e0acaf09fb` and `SeedRng` hash `77dddf4b6256d28fe54fe4fa7c41a15d549d1d3e086013e03c7919823fda7edb`.

Japanese rev0/rev1 use distinct addresses and state locations; English revisions use `$03005000`; German, French, Italian and Spanish use `$03004F50`. Every release independently proves the same 32-bit ISO-C recurrence and upper-16-bit result.

Naming is corroborated by `pret/pokefirered@037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/random.c`. Reports publish no ROM bytes.

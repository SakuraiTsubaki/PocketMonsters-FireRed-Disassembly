# Pokemon FireRed EnableVCountIntrAtLine150 disassembly

The Japanese release `bpr-j-rev0-retail` is the origin reference. Independent ROM scanning found exactly one matching 40-byte Thumb routine in every one of the 8 cataloged releases (Japanese, English, German, French, Italian, Spanish). Ruby and Sapphire were checked separately and do not contain this routine shape.

The assembly preserves the low DISPSTAT byte, installs VCount line 150 and its enable bit, then enables interrupt flag 0x0004. Per-release CFGs omit raw instruction halfwords; maps retain only locations, hashes, constants and call targets. Names are corroborated by `pret/pokefirered` at `037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/main.c`.

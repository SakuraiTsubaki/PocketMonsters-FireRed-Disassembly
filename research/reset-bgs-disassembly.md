# FireRed ResetBgs disassembly

`bpr-j-rev0-retail` is the Japanese origin reference. All 8 cataloged releases (Japanese, English, German, French, Italian, Spanish) resolve the boot call immediately after ClearDma3Requests. Each 20-byte wrapper resets BG control structures, clears DISPCNT, then selects text mode and hides BGs. Maps preserve addresses, call targets and hashes without ROM bytes.

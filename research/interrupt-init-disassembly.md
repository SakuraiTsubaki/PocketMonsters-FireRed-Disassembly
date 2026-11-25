# Pokemon FireRed interrupt initialization disassembly

`bpr-j-rev0-retail` is the Japanese origin reference. All 8 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain one InitIntrHandlers suite matching the `frlg` profile. VBlank is enabled through EnableInterrupts. The routine copies 14 table entries, DMA-copies the 0x800-byte dispatcher with DMA3 control 0x84000200, installs the IWRAM vector, clears callbacks and enables VBlank. Evidence omits ROM bytes and instruction halfwords.

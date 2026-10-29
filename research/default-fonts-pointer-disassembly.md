# FireRed SetDefaultFontsPointer disassembly

`bpr-j-rev0-retail` is the Japanese origin reference. All 8 cataloged releases (Japanese, English, German, French, Italian, Spanish) preserve the 12-byte wrapper that loads `gFontInfos` and calls SetFontsPointer. Family-specific boot ordering around InitHeap is independently checked. Maps publish only addresses, structure and hashes, never ROM bytes or instruction halfwords.

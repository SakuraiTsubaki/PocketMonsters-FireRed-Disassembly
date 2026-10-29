# FireRed InitHeap disassembly

`bpr-j-rev0-retail` is the Japanese origin reference. All 8 cataloged releases (Japanese, English, German, French, Italian, Spanish) preserve the 18-byte arena bootstrap that stores the heap start and size before calling PutFirstMemBlockHeader. The family-specific boot order uses 1 call(s) after ResetBgs. Maps retain addresses and hashes without ROM bytes.

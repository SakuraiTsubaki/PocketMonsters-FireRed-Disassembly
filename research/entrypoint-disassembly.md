# Japanese ROM entry disassembly

The exact-hash Japanese revision 0 ROM begins with little-endian bytes `7f0000ea`, decoded independently as ARM instruction `b 0x08000204` at `0x08000000` (word `0xea00007f`). The shared Disassembly tool re-encodes the target and requires an exact word match before setting `round_trip_verified`.

`src/rom_entry.s` preserves this first instruction byte-for-byte. This establishes only the entry branch and does not import or imply Decompilation reconstruction state. The release remains a candidate.


# Japanese Thumb entry reachable disassembly

Starting at the proven Thumb transition target `0x080003a4`, conservative control-flow traversal records 116 reachable halfwords, 12 direct CFG edges, and 29 BL call sites. BL targets are recorded without following callees, and unreachable gaps are represented by explicit `.org` directives in the source.

The source halfwords in ascending address order have canonical SHA-256 `297af8ff1b2ef3c0b9509e3c098af603f4b7643afd2b7d7264f61c9ac512012c`. No return is reachable in this graph, so this is documented as a non-returning bootstrap path rather than a complete function boundary. Every emitted `.hword` is checked against its original little-endian ROM bytes.


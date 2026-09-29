# Japanese ARM bootstrap disassembly

Starting at the independently decoded entry target `0x08000204`, twelve ARM words end at `bx r1` at `0x08000230`. The latest PC-relative load into `r1` reads literal `0x080003a5` from `0x08000244`, proving a Thumb-state transition to aligned address `0x080003a4`.

The exact 48-byte instruction range has SHA-256 `d351dac18b97db56c30ec6b71463a08edde9480d27fb2c48bdda135efec937e6`. `src/rom_bootstrap.s` preserves all twelve words byte-for-byte; literal data outside that range remains represented only as verified address/value evidence. This Disassembly result is independently generated and does not import Decompilation source state.


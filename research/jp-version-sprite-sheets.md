# Japanese version-specific 4bpp sprite sheets

Target: BPRJ-rev0 (1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486)

A bounded scan of the verified Japanese ROM identified valid BIOS-LZ77 streams in the version-specific late-ROM region. Cross-version comparison showed that most nearby 4,096/8,192-byte decoded streams are identical between FireRed and LeafGreen, while the two streams recorded here differ in both compressed and decoded hashes and visibly contain version-dependent character/large-form graphics.

The two 4,096-byte outputs begin at `0xD3958C` and `0xD39D70`. Each decodes to 128 4bpp tiles and is rendered in ROM tile order as a 16×8 tile sheet. The PNGs intentionally use a deterministic grayscale index preview because the matching runtime palette has not yet been proven; no speculative color palette is attached.

The extractor gates the full ROM SHA-256 and records the compressed source-range hash, decoded tile hash, PNG hash, format, dimensions, and source offset. Raw compressed or decoded ROM bytes are not stored. The neutral `version-sprite-sheet` label preserves what is proven without assigning an unverified scene or animation name.


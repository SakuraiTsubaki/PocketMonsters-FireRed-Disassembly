# FireRed English game-title logo

The public `pret/pokefirered` title-logo asset is an English-build asset. Its
8x8 tile-order conversion did not match an equivalent 16,384-byte LZ77 stream
in the Japanese revision-0 ROM, so it is not mislabeled as Japanese evidence.

It exactly matches the English revision-0 candidate (`BPRE`) stream at
`0xEAB8C4`. Decompression yields 16,384 bytes (256 8bpp tiles), SHA-256
`c31453fde1834af792e49e675d0b47683e9312c637683fad0f3ebe4177bc7a9c`.
The colored public PNG uses the corresponding 256-color JASC palette.

The common 8bpp extractor gates the ROM SHA-256, records compressed and
decoded hashes, and emits the PNG without publishing ROM bytes. This asset
match does not promote the complete release candidate to `verified`.

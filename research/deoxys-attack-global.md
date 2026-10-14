# Global Deoxys Attack Forme sprites

The English, German, French, Italian, and Spanish rev0 releases were checked independently against their pinned ROM SHA-256 identities. In every release, the compressed sheets at the recorded offsets resolve to species 410 (`SPECIES_DEOXYS`) entries with size `0x0800` in the runtime front- and back-pic tables. The front tables have 28 or 29 decoded Thumb references depending on the localization; every back table has 9.

All five releases decode to the same Attack Forme pixels as Japanese rev0: front SHA-256 `ed6b7c3b3be626897d54ac922eee955f0616611cbe7eeafb416bf5e2623882e0` and back SHA-256 `76478bca4bc91a53cee1c2704aa83877b6bca240a24dd127b11c8ba03a276225`. Their 16-color palette also decodes identically. The repository preserves a color PNG and JASC palette for every verified release, plus release-specific compression and table reports; shared image hashes are expected evidence, not deduplication assumptions.

Together with the separate Japanese rev0 and Japanese/English rev1 evidence, this covers every catalogued FireRed retail ROM currently available to the project. No ROM bytes or decoded binary sheets are published.

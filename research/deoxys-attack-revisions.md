# Deoxys Attack Forme in remaining FireRed revisions

The BPRJ rev1 and BPRE rev1 ROMs were SHA-256 gated against `research/releases.csv`. Exact decoded-hash searches locate one front stream, one back stream, and one 16-color palette in each release. Their decoded hashes match the established Japanese rev0 Attack Forme assets and the palette/PNG reconstructions are byte-identical.

The ROM tables independently identify both graphics as species tag `0x019A` (410, Deoxys) with size `0x0800`. BPRJ rev1 uses front/back table bases `0x1EFEA8` and `0x1F1348`; BPRE rev1 uses `0x23511C` and `0x2365BC`. Each front table base has 28 Thumb literal consumers and each back table base has 9.

Together with the existing rev0 Japanese and five global-language reports, all eight catalogued FireRed releases now have asset identity evidence. Color PNGs are shared only after byte-exact reconstruction; no ROM binary is stored and candidate status is unchanged.

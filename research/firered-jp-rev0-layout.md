# FireRed Japanese revision 0 layout measurement

The 16 MiB Japanese origin candidate is measured as sixteen 1 MiB regions. Regions 7–11 and 14 are uniform `0xff` padding, producing 11 distinct region hashes; region 0 is only `header-and-entry`, and all remaining non-padding regions stay `unclassified`. Counts of pointer and branch-like words are search evidence, not code/data proof. No ROM bytes are stored and the release remains a `candidate`.

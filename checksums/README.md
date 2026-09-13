# Checksum Verification

This directory stores verified checksum manifests for supported FireRed baselines.

## Policy

- Do not copy checksum values from unverified secondary lists and label them canonical.
- Compute hashes directly from the project's read-only reference ROMs.
- Record at least SHA-1 and SHA-256 for each verified baseline.
- Record file size and relevant GBA header identity fields alongside hashes.
- Recompute the same hashes for every repository-built ROM.
- A baseline is considered byte-perfect only when the generated ROM matches the verified reference hash exactly.

No retail or rebuilt ROM image is stored in this directory.

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class DeoxysAttackGlobalTests(unittest.TestCase):
    def test_release_assets_and_tables(self):
        manifest = json.loads((ROOT / "manifests/deoxys-attack-global.json").read_text())
        shared = manifest["shared_hashes"]
        for language, release in manifest["releases"].items():
            palette = json.loads((ROOT / f"analysis/firered-{language}-rev0-deoxys-palette.json").read_text())
            self.assertEqual(palette["rom_sha256"], release["sha256"])
            self.assertEqual(palette["source_offset"], release["palette_source"])
            self.assertEqual(palette["decompressed_sha256"], shared["palette_decoded_sha256"])
            palette_path = ROOT / f"graphics/pokemon/deoxys-normal-{language}.pal"
            self.assertEqual(hashlib.sha256(palette_path.read_bytes()).hexdigest(), shared["palette_sha256"])
            for role, refs in (("front", (28, 29)), ("back", (9,))):
                asset = json.loads((ROOT / f"analysis/firered-{language}-rev0-deoxys-attack-{role}.json").read_text())
                table = json.loads((ROOT / f"analysis/firered-{language}-rev0-deoxys-{role}-table.json").read_text())
                entry = table["entries"][0]
                self.assertEqual(asset["rom_sha256"], release["sha256"])
                self.assertEqual(asset["source_offset"], release[f"{role}_source"])
                self.assertEqual(asset["decompressed_sha256"], shared[f"{role}_decoded_sha256"])
                self.assertEqual((entry["table_offset"], entry["size"], entry["tag"]), (release[f"{role}_table"], 0x800, 410))
                self.assertIn(len(entry["table_thumb_references"]), refs)
                png = ROOT / f"graphics/pokemon/deoxys-attack-{role}-{language}.png"
                self.assertEqual(hashlib.sha256(png.read_bytes()).hexdigest(), shared[f"{role}_png_sha256"])

    def test_manifest_has_no_rom_payload(self):
        manifest = json.loads((ROOT / "manifests/deoxys-attack-global.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        self.assertEqual(set(manifest["releases"]), {"en", "de", "fr", "it", "es"})


if __name__ == "__main__":
    unittest.main()

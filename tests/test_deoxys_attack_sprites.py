import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
ROM_SHA = "1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486"


class DeoxysAttackSpriteTests(unittest.TestCase):
    def test_species_tables(self):
        expected = {
            "front": (0xD3958C, 0x1F5360, 0x1F4690, 28),
            "back": (0xD39D70, 0x1F6800, 0x1F5B30, 9),
        }
        for role, (source, entry, table, refs) in expected.items():
            report = json.loads((ROOT / "analysis" / f"firered-jp-rev0-deoxys-{role}-table.json").read_text())
            self.assertEqual(report["source_sha256"], ROM_SHA)
            self.assertEqual(report["asset"]["source_offset"], source)
            item = report["entries"][0]
            self.assertEqual((item["entry_offset"], item["table_offset"]), (entry, table))
            self.assertEqual((item["size"], item["tag"]), (0x800, 410))
            self.assertEqual(len(item["table_thumb_references"]), refs)

    def test_palette_and_color_outputs(self):
        palette = json.loads((ROOT / "analysis/firered-jp-rev0-deoxys-palette.json").read_text())
        self.assertEqual((palette["source_offset"], palette["color_count"]), (0xD39D48, 16))
        self.assertEqual(palette["rom_sha256"], ROM_SHA)
        self.assertEqual(hashlib.sha256((ROOT / "graphics/pokemon/deoxys-normal-jp.pal").read_bytes()).hexdigest(), palette["palette_sha256"])
        for role in ("front", "back"):
            report = json.loads((ROOT / "analysis" / f"firered-jp-rev0-deoxys-attack-{role}.json").read_text())
            png = ROOT / "graphics/pokemon" / f"deoxys-attack-{role}-jp.png"
            self.assertEqual(report["palette"], "jasc-pal")
            self.assertEqual(report["palette_sha256"], palette["palette_sha256"])
            self.assertEqual(hashlib.sha256(png.read_bytes()).hexdigest(), report["png_sha256"])

    def test_manifest(self):
        manifest = json.loads((ROOT / "manifests/deoxys-attack-sprites.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()

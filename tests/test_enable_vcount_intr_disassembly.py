import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]


class VCountInterruptDisassemblyTests(unittest.TestCase):
    def test_all_catalog_releases(self):
        catalog_name = next((ROOT / "analysis").glob("*-global-release-catalog.json"))
        catalog = json.loads(catalog_name.read_text(encoding="utf-8"))
        summary = json.loads((ROOT / "analysis/enable-vcount-intr-at-line150-disassembly-summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["axis"], "disassembly")
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(summary["origin_reference"], catalog["releases"][0]["id"])
        for release in catalog["releases"]:
            release_id = release["id"]
            mapping = json.loads((ROOT / f"analysis/{release_id}-enable-vcount-intr-at-line150-map.json").read_text(encoding="utf-8"))
            cfg = json.loads((ROOT / f"analysis/{release_id}-enable-vcount-intr-at-line150-cfg.json").read_text(encoding="utf-8"))
            self.assertEqual(mapping["axis"], "disassembly")
            self.assertEqual(mapping["target"]["sha256"], release["sha256"])
            self.assertEqual([call["name"] for call in mapping["calls"]], ["GetGpuReg", "SetGpuReg", "EnableInterrupts"])
            self.assertEqual(mapping["function"]["rom_code_range"]["length"], 40)
            self.assertEqual(mapping["constants"]["vcount_compare_line"], 150)
            self.assertNotIn("halfword", cfg["instructions"][0])
            self.assertFalse(mapping["raw_rom_bytes_included"])

    def test_source_and_manifest(self):
        source = (ROOT / "src/enable_vcount_intr_at_line150.s").read_text(encoding="utf-8")
        self.assertIn(".thumb_func", source)
        self.assertIn("movs r2, #150", source)
        manifest = json.loads((ROOT / "manifests/enable-vcount-intr-disassembly.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["axis"], "disassembly")
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()


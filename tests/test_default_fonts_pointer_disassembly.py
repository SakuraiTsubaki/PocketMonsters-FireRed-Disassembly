import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]

class DefaultFontsPointerDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_maps(self):
        summary = json.loads((ROOT / "analysis/default-fonts-pointer-disassembly-summary.json").read_text())
        catalogs = list((ROOT / "analysis").glob("*-global-release-catalog.json"))
        self.assertEqual(len(catalogs), 1)
        catalog = json.loads(catalogs[0].read_text())
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            behavior = evidence["verified_behavior"]
            self.assertEqual(evidence["function"]["rom_code_range"]["length"], 12)
            self.assertEqual(evidence["function"]["calls"][0]["name"], "SetFontsPointer")
            self.assertEqual(behavior["default_table_name"], "gFontInfos")
            self.assertTrue(behavior["default_table_address"].startswith("0x08"))
            self.assertEqual(behavior["callee_shape"], [6, 3, 0, 1, 0])
            self.assertTrue(evidence["control_flow"]["raw_halfwords_omitted"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/default-fonts-pointer-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])

    def test_source_selects_default_table(self):
        source = (ROOT / "src/set_default_fonts_pointer.s").read_text()
        for token in ("SetDefaultFontsPointer:", "gFontInfos", "SetFontsPointer"):
            self.assertIn(token, source)

if __name__ == "__main__":
    unittest.main()


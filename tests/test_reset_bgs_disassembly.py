import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]

class ResetBgsDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_maps(self):
        summary = json.loads((ROOT / "analysis/reset-bgs-disassembly-summary.json").read_text())
        catalogs = list((ROOT / "analysis").glob("*-global-release-catalog.json"))
        self.assertEqual(len(catalogs), 1)
        catalog = json.loads(catalogs[0].read_text())
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["function"]["rom_code_range"]["length"], 20)
            self.assertEqual([call["name"] for call in evidence["function"]["calls"]],
                             ["ResetBgControlStructs", "SetTextModeAndHideBgs"])
            self.assertTrue(evidence["verified_behavior"]["sGpuBgConfigs_address"].startswith("0x030"))
            self.assertEqual(evidence["verified_behavior"]["bgVisibilityAndMode_value"], 0)
            self.assertTrue(evidence["control_flow"]["raw_halfwords_omitted"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/reset-bgs-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])

    def test_source_preserves_reset_sequence(self):
        source = (ROOT / "src/reset_bgs.s").read_text()
        for token in ("ResetBgs:", "ResetBgControlStructs", "sGpuBgConfigs",
                      "strh r0, [r1, #0x10]", "SetTextModeAndHideBgs"):
            self.assertIn(token, source)

if __name__ == "__main__":
    unittest.main()

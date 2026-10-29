import hashlib
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class ClearDma3RequestsDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_maps(self):
        summary = json.loads((ROOT / "analysis/clear-dma3-requests-disassembly-summary.json").read_text())
        catalogs = list((ROOT / "analysis").glob("*-global-release-catalog.json"))
        self.assertEqual(len(catalogs), 1)
        catalog = json.loads(catalogs[0].read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            behavior = evidence["verified_behavior"]
            self.assertEqual(evidence["function"]["rom_code_range"]["length"], 42)
            self.assertEqual(behavior["instruction_form"], "lock-clear-128-requests-unlock")
            self.assertEqual(behavior["request_count"], 128)
            self.assertEqual(behavior["request_stride"], 16)
            self.assertEqual(behavior["cleared_offsets"], [8, 0, 4])
            self.assertTrue(evidence["control_flow"]["raw_halfwords_omitted"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/clear-dma3-requests-disassembly.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            actual = hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest()
            self.assertEqual(actual, output["sha256"])

    def test_source_preserves_request_clear_loop(self):
        source = (ROOT / "src/clear_dma3_requests.s").read_text()
        for token in ("ClearDma3Requests:", "sDma3ManagerLocked",
                      "sDma3RequestCursor", "sDma3Requests", "#0x7f",
                      "strh r3, [r0, #8]", "adds r0, #0x10"):
            self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()


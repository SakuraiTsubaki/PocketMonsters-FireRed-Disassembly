import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]

class InitHeapDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_maps(self):
        summary = json.loads((ROOT / "analysis/init-heap-disassembly-summary.json").read_text())
        catalogs = list((ROOT / "analysis").glob("*-global-release-catalog.json"))
        self.assertEqual(len(catalogs), 1)
        catalog = json.loads(catalogs[0].read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            behavior = evidence["verified_behavior"]
            self.assertEqual(evidence["function"]["rom_code_range"]["length"], 18)
            self.assertEqual(evidence["function"]["calls"][0]["name"],
                             "PutFirstMemBlockHeader")
            self.assertEqual(behavior["instruction_form"],
                             "record-arena-then-first-block")
            self.assertTrue(behavior["sHeapStart_address"].startswith("0x030"))
            self.assertTrue(behavior["sHeapSize_address"].startswith("0x030"))
            self.assertTrue(evidence["control_flow"]["raw_halfwords_omitted"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/init-heap-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])

    def test_source_preserves_heap_bootstrap(self):
        source = (ROOT / "src/init_heap.s").read_text()
        for token in ("InitHeap:", "sHeapStart", "sHeapSize", "PutFirstMemBlockHeader"):
            self.assertIn(token, source)

if __name__ == "__main__":
    unittest.main()


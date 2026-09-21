from __future__ import annotations
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class LayoutAnalysisTests(unittest.TestCase):
 def test_origin_layout_is_complete_and_conservative(self):
  r=json.loads((ROOT/"analysis"/"firered-jp-rev0-layout.json").read_text(encoding="utf-8"));self.assertEqual(r["sha256"],"1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486");self.assertEqual(r["region_count"],16);self.assertEqual([x["region"] for x in r["regions"] if x["classification"]=="padding"],[7,8,9,10,11,14]);self.assertEqual(len({x["sha256"] for x in r["regions"]}),11)
 def test_manifest_hashes_output(self):
  m=json.loads((ROOT/"analysis"/"firered-jp-rev0-layout-manifest.json").read_text(encoding="utf-8"));o=m["outputs"][0];self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
if __name__=="__main__":unittest.main()

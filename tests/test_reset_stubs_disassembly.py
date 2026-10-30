import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/reset-stubs-summary.json").read_text());self.assertEqual(s["release_count"],8)
  for r in s["releases"]:e=json.loads((ROOT/r["evidence"]).read_text());self.assertEqual(e["functions"]["SoftReset"]["reset_stack_pointer"],"0x03007F00")
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/reset-stubs-disassembly.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()

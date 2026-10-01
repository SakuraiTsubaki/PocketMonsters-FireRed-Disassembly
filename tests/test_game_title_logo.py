import hashlib,json,struct,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_manifest_report_and_outputs(self):
  m=json.loads((ROOT/'manifests/game-title-logo-en.json').read_text());r=json.loads((ROOT/'analysis/firered-en-rev0-game-title-logo.json').read_text())
  self.assertEqual(m['source']['offset'],f"0x{r['source_offset']:X}");self.assertEqual(m['decoded']['sha256'],r['decompressed_sha256']);self.assertFalse(m['raw_rom_bytes_included'])
  for output in m['outputs'][:2]: self.assertEqual(hashlib.sha256((ROOT/output['path']).read_bytes()).hexdigest(),output['sha256'])
 def test_png(self):
  png=(ROOT/'graphics/title/game-title-logo-en.png').read_bytes();self.assertEqual(struct.unpack('>II',png[16:24]),(256,64));self.assertEqual(png[25],2)
if __name__=='__main__': unittest.main()

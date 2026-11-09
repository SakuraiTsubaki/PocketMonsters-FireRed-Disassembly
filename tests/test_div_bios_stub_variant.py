import hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_variant(self):
  s=json.loads((R/'analysis/div-bios-stub-variant-summary.json').read_text());self.assertEqual((s['release_count'],s['present_release_count'],s['absent_release_count'],s['origin_availability']),(8,6,2,'absent'))
  for x in s['releases']:
   e=json.loads((R/x['evidence']).read_text());self.assertEqual(e['target']['sha256'],x['sha256']);self.assertFalse(e['raw_rom_bytes_included'])
   if x['language']=='Japanese':self.assertEqual((x['availability'],e['function'],e['source_applies']),('absent',None,False))
   else:self.assertEqual((x['availability'],e['function']['software_interrupt'],e['function']['lz77_vram_relative_offset'],e['source_applies']),('present',6,-4,True))
 def test_manifest(self):
  m=json.loads((R/'manifests/div-bios-stub-variant.json').read_text());
  for x in m['outputs']:self.assertEqual(hashlib.sha256((R/x['path']).read_bytes()).hexdigest(),x['sha256'])
if __name__=='__main__':unittest.main()

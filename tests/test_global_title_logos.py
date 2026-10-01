import hashlib,json,struct,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_assets_and_reports(self):
  m=json.loads((ROOT/'manifests/game-title-logos-global.json').read_text());self.assertEqual(m['languages'],['de','fr','it','es']);self.assertFalse(m['raw_rom_bytes_included'])
  for a in m['assets']:
   lang=a['language'];tiles=json.loads((ROOT/'analysis'/f'firered-{lang}-rev0-game-title-logo.json').read_text());pal=json.loads((ROOT/'analysis'/f'firered-{lang}-rev0-game-title-logo-palette.json').read_text())
   self.assertEqual(a['tiles']['decompressed_sha256'],tiles['decompressed_sha256']);self.assertEqual(a['palette']['source_sha256'],pal['source_sha256'])
   for part in ('tiles','palette'): self.assertEqual(hashlib.sha256((ROOT/a[part]['path']).read_bytes()).hexdigest(),a[part]['png_sha256' if part=='tiles' else 'output_sha256'])
   png=(ROOT/a['tiles']['path']).read_bytes();self.assertEqual(struct.unpack('>II',png[16:24]),(256,64));self.assertEqual(png[25],2)
if __name__=='__main__':unittest.main()

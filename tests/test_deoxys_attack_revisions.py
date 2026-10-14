import hashlib, json, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
CASES={
 "jp-rev1":("cec5fc4dbe38cd8026bd6664a1a041d9dc91e8d4249bab04e7bde70c3cdf4e06",0xD3958C,0xD39D70,0x1EFEA8,0x1F1348),
 "en-rev1":("6d306e01ba04907efaa0611a32fee3b440a1e8ac8b4e0acdd223dc9281afa170",0xE3958C,0xE39D70,0x23511C,0x2365BC),
}
class Tests(unittest.TestCase):
 def test_assets_tables_and_palette(self):
  for release,(sha,front,back,ftable,btable) in CASES.items():
   pal=json.loads((ROOT/f'analysis/firered-{release}-deoxys-palette.json').read_text());self.assertEqual(pal['rom_sha256'],sha);self.assertEqual(pal['palette_sha256'],'479c76fdaf9a0ca458fa37a514b9bbf20d9dc3c7b82d813ea743e4830a58f197')
   for role,offset,table,refs in (('front',front,ftable,28),('back',back,btable,9)):
    asset=json.loads((ROOT/f'analysis/firered-{release}-deoxys-attack-{role}.json').read_text());e=json.loads((ROOT/f'analysis/firered-{release}-deoxys-{role}-table.json').read_text())['entries'][0]
    self.assertEqual(asset['rom_sha256'],sha);self.assertEqual(asset['source_offset'],offset);self.assertEqual(asset['palette'],'jasc-pal');self.assertEqual((e['table_offset'],e['size'],e['tag']),(table,0x800,410));self.assertEqual(len(e['table_thumb_references']),refs)
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/deoxys-attack-revisions.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()

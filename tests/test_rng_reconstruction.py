import csv,hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
ADDR={'firered-jp-rev0':(0x0804448C,'0x03005040'),'firered-jp-rev1':(0x08044468,'0x03004FA0'),'firered-en-rev0':(0x08044EC8,'0x03005000'),'firered-en-rev1':(0x08044EDC,'0x03005000'),'firered-de-rev0':(0x08044DCC,'0x03004F50'),'firered-fr-rev0':(0x08044E8C,'0x03004F50'),'firered-it-rev0':(0x08044DB8,'0x03004F50'),'firered-es-rev0':(0x08044EA0,'0x03004F50')}
class Tests(unittest.TestCase):
 def test_all_releases(self):
  rows={r['id']:r for r in csv.DictReader((ROOT/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(ADDR))
  for release,(address,state) in ADDR.items():
   m=json.loads((ROOT/f'analysis/{release}-rng.json').read_text());self.assertEqual(m['target']['sha256'],rows[release]['sha256']);self.assertEqual((m['functions']['Random']['address'],m['globals']['gRngValue']),(f'0x{address:08X}',state));self.assertEqual(m['functions']['SeedRng']['rom_offset']-m['functions']['Random']['rom_offset'],32);self.assertEqual(m['functions']['Random']['code_sha256'],'72526af8af03e60317e6ac115ece4a9415af188772c5432ec1c145e0acaf09fb')
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/rng-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()

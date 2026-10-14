import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
PREFIX = "firered"


class GameTitleLogoLoaderTests(unittest.TestCase):
    def setUp(self):
        self.assets = sorted(
            (ROOT / "analysis").glob(f"{PREFIX}-*-game-title-logo.json")
        )
        self.manifest = json.loads(
            (ROOT / "manifests/game-title-logo-loaders.json").read_text()
        )
        self.source = (ROOT / "src/game_title_logo_loader.asm").read_text()

    def test_all_localized_assets_have_one_bg_load(self):
        self.assertEqual(len(self.assets), 5)
        for asset_path in self.assets:
            asset = json.loads(asset_path.read_text())
            load = json.loads(
                asset_path.with_name(asset_path.stem + "-load.json").read_text()
            )
            self.assertEqual(load["source_sha256"], asset["rom_sha256"])
            self.assertEqual(load["asset"]["source_offset"], asset["source_offset"])
            self.assertEqual(len(load["pointer_locations"]), 1)
            self.assertEqual(len(load["background_loads"]), 1)
            self.assertFalse(load["raw_bytes_published"])

    def test_call_uses_bg_zero_tile_transfer_arguments(self):
        for asset_path in self.assets:
            load = json.loads(
                asset_path.with_name(asset_path.stem + "-load.json").read_text()
            )["background_loads"][0]
            self.assertEqual(load["asset_argument_register"], 1)
            self.assertEqual(
                {key: load["register_immediates"][key] for key in ("r0", "r2", "r3")},
                {"r0": 0, "r2": 0, "r3": 0},
            )
            self.assertEqual(load["loader_sequence_length"], 16)
            self.assertGreaterEqual(load["call_target"], 0x08000000)
            self.assertLess(load["call_target"], 0x0A000000)

    def test_semantic_source_names_runtime_api(self):
        self.assertIn("LoadGameTitleLogoTiles::", self.source)
        self.assertIn("ldr r1, =GameTitleLogoTiles", self.source)
        self.assertIn("bl DecompressAndCopyTileDataToVram", self.source)

    def test_manifest_hashes_outputs(self):
        self.assertFalse(self.manifest["raw_rom_bytes_included"])
        for output in self.manifest["outputs"]:
            self.assertEqual(
                hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                output["sha256"],
            )


if __name__ == "__main__":
    unittest.main()

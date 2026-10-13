from __future__ import annotations

import hashlib
import json
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("en", "de", "fr", "it", "es")
ROM_SHA256 = {
    "en": "b59a65bb439b7dfdf2ffbbe5102be03de2501a71f5e081eec1c76f9d2ef3ba00",
    "de": "eed4fb0242bcbb6e0b0b80b197b47e3aec99ef4c5562cc45bae50ae86b970507",
    "fr": "245866842349cedbe2a034c6d20438d26d18b627b3d0909d7cb795fc87d7675a",
    "it": "ad52b593ef0c7439e1409d3f0a1ec3ff865a494ca46c2184fe65573759838f3a",
    "es": "ab696c065639e4d73c3c3ed9d4fbf9c7fed593761f3b6746256ff82465596554",
}
OFFSETS = {
    "en": (0xE3958C, 0xE39D70),
    "de": (0xE39580, 0xE39D64),
    "fr": (0xE3958C, 0xE39D70),
    "it": (0xE39584, 0xE39D68),
    "es": (0xE3958C, 0xE39D70),
}


class GlobalVersionSpriteSheetTests(unittest.TestCase):
    def test_reports_match_release_and_japanese_reference(self):
        jp = [
            json.loads((ROOT / "analysis" / f"firered-jp-version-sprite-sheet-{sheet}.json").read_text())
            for sheet in range(2)
        ]
        for language in LANGUAGES:
            for sheet in range(2):
                report = json.loads(
                    (ROOT / "analysis" / f"firered-{language}-version-sprite-sheet-{sheet}.json").read_text()
                )
                png = ROOT / "graphics" / "title" / f"{language}-version-sprite-sheet-{sheet}.png"
                self.assertEqual(report["rom_sha256"], ROM_SHA256[language])
                self.assertEqual(report["source_offset"], OFFSETS[language][sheet])
                self.assertEqual(report["compressed_sha256"], jp[sheet]["compressed_sha256"])
                self.assertEqual(report["decompressed_sha256"], jp[sheet]["decompressed_sha256"])
                self.assertEqual(report["decompressed_length"], 4096)
                self.assertEqual(report["tile_count"], 128)
                self.assertEqual(report["tiles_per_row"], 16)
                self.assertEqual(report["palette"], "grayscale-index-preview")
                self.assertFalse(report["raw_rom_bytes_included"])
                self.assertEqual(hashlib.sha256(png.read_bytes()).hexdigest(), report["png_sha256"])
                self.assertEqual(struct.unpack(">II", png.read_bytes()[16:24]), (256, 128))

    def test_manifest_outputs(self):
        manifest = json.loads((ROOT / "manifests" / "global-version-sprite-sheets.json").read_text())
        self.assertEqual(manifest["languages"], list(LANGUAGES))
        self.assertEqual({item["language"] for item in manifest["releases"]}, set(LANGUAGES))
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()

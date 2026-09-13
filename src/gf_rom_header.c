#include "gf_rom_header.h"

#ifndef GAME_LANGUAGE
#error GAME_LANGUAGE is required
#endif

extern const uint8_t gMonFrontPicTable[];
extern const uint8_t gMonBackPicTable[];
extern const uint8_t gMonPaletteTable[];
extern const uint8_t gMonShinyPaletteTable[];
extern const uint8_t gMonIconTable[];
extern const uint8_t gMonIconPaletteIndices[];
extern const uint8_t gMonIconPaletteTable[];
extern const uint8_t gSpeciesNames[];
extern const uint8_t gMoveNames[];
extern const uint8_t gDecorations[];
extern const uint8_t gSpeciesInfo[];
extern const uint8_t gAbilityNames[];
extern const uint8_t gAbilityDescriptionPointers[];
extern const uint8_t gItems[];
extern const uint8_t gBattleMoves[];
extern const uint8_t gBallSpriteSheets[];
extern const uint8_t gBallSpritePalettes[];

#if GAME_LANGUAGE == 1
#define GF_FIELD_075 5
#define GF_POKEMON_NAME_LENGTH_2 5
#define GF_FIELD_078 7
#define GF_FIELD_079 8
#define GF_FIELD_07B 7
#define GF_FIELD_07C 4
#define GF_FIELD_07D 10
#define GF_FIELD_07F 10
#define GF_FIELD_080 10
#define GF_FIELD_081 5
#define GF_FIELD_083 3
#define GF_FIELD_084 7
#define GF_SAVE_BLOCK_1_SIZE 0x3D40
#else
#define GF_FIELD_075 10
#define GF_POKEMON_NAME_LENGTH_2 10
#define GF_FIELD_078 12
#define GF_FIELD_079 12
#define GF_FIELD_07B 12
#define GF_FIELD_07C 6
#define GF_FIELD_07D 16
#define GF_FIELD_07F 12
#define GF_FIELD_080 15
#define GF_FIELD_081 11
#define GF_FIELD_083 8
#define GF_FIELD_084 12
#define GF_SAVE_BLOCK_1_SIZE 0x3D68
#endif

#define ROMPTR(symbol) ((uint32_t)(uintptr_t)(symbol))

__attribute__((section(".text.consts"), used, aligned(4)))
const struct GfRomHeader gGfRomHeader = {
    .version = 4,
    .language = GAME_LANGUAGE,
    .gameName = "pokemon red version",
    .monFrontPics = ROMPTR(gMonFrontPicTable),
    .monBackPics = ROMPTR(gMonBackPicTable),
    .monNormalPalettes = ROMPTR(gMonPaletteTable),
    .monShinyPalettes = ROMPTR(gMonShinyPaletteTable),
    .monIcons = ROMPTR(gMonIconTable),
    .monIconPaletteIds = ROMPTR(gMonIconPaletteIndices),
    .monIconPalettes = ROMPTR(gMonIconPaletteTable),
    .monSpeciesNames = ROMPTR(gSpeciesNames),
    .moveNames = ROMPTR(gMoveNames),
    .decorations = ROMPTR(gDecorations),
    .flagsOffset = 0xEE0,
    .varsOffset = 0x1000,
    .pokedexOffset = 0x18,
    .seen1Offset = 0x5F8,
    .seen2Offset = 0x3A18,
    .pokedexVar = 0x3C,
    .pokedexFlag = 0x838,
    .mysteryGiftFlag = 0x839,
    .pokedexCount = 386,
    .playerNameLength = 7,
    .field_075 = GF_FIELD_075,
    .pokemonNameLength1 = 10,
    .pokemonNameLength2 = GF_POKEMON_NAME_LENGTH_2,
    .field_078 = GF_FIELD_078,
    .field_079 = GF_FIELD_079,
    .field_07A = 6,
    .field_07B = GF_FIELD_07B,
    .field_07C = GF_FIELD_07C,
    .field_07D = GF_FIELD_07D,
    .field_07E = 18,
    .field_07F = GF_FIELD_07F,
    .field_080 = GF_FIELD_080,
    .field_081 = GF_FIELD_081,
    .field_082 = 1,
    .field_083 = GF_FIELD_083,
    .field_084 = GF_FIELD_084,
    .saveBlock2Size = 0xF24,
    .saveBlock1Size = GF_SAVE_BLOCK_1_SIZE,
    .partyCountOffset = 0x34,
    .partyOffset = 0x38,
    .warpFlagsOffset = 9,
    .trainerIdOffset = 0xA,
    .playerNameOffset = 0,
    .playerGenderOffset = 8,
    .field_0A8 = 0xAD,
    .field_0AC = 0xAD,
    .externalEventFlagsOffset = 0x30BB,
    .externalEventDataOffset = 0x30A7,
    .field_0B8 = 0,
    .speciesInfo = ROMPTR(gSpeciesInfo),
    .abilityNames = ROMPTR(gAbilityNames),
    .abilityDescriptions = ROMPTR(gAbilityDescriptionPointers),
    .items = ROMPTR(gItems),
    .moves = ROMPTR(gBattleMoves),
    .ballGfx = ROMPTR(gBallSpriteSheets),
    .ballPalettes = ROMPTR(gBallSpritePalettes),
    .gcnLinkFlagsOffset = 0xA8,
    .gameClearFlag = 0x82C,
    .ribbonFlag = 0x83B,
    .bagCountItems = 42,
    .bagCountKeyItems = 30,
    .bagCountPokeballs = 13,
    .bagCountTMHMs = 58,
    .bagCountBerries = 43,
    .pcItemsCount = 30,
    .pcItemsOffset = 0x298,
    .giftRibbonsOffset = 0x309C,
    .enigmaBerryOffset = 0x30EC,
    .enigmaBerrySize = 0x34,
    .moveDescriptions = 0,
    .field_100 = 0xFFFFFFFF,
};

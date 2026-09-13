#ifndef GUARD_GF_ROM_HEADER_H
#define GUARD_GF_ROM_HEADER_H

#include <stdint.h>

/*
 * FireRed Game Freak compatibility header found at ROM 0x100..0x203.
 * Pointer fields are stored as 32-bit GBA ROM addresses in the built image.
 * Unknown byte fields retain offset-based names until their semantics are
 * independently verified.
 */
struct GfRomHeader
{
    uint32_t version;                    /* 0x000 */
    uint32_t language;                   /* 0x004 */
    uint8_t gameName[32];                /* 0x008 */
    uint32_t monFrontPics;               /* 0x028 */
    uint32_t monBackPics;                /* 0x02C */
    uint32_t monNormalPalettes;          /* 0x030 */
    uint32_t monShinyPalettes;           /* 0x034 */
    uint32_t monIcons;                   /* 0x038 */
    uint32_t monIconPaletteIds;          /* 0x03C */
    uint32_t monIconPalettes;            /* 0x040 */
    uint32_t monSpeciesNames;            /* 0x044 */
    uint32_t moveNames;                  /* 0x048 */
    uint32_t decorations;                /* 0x04C */
    uint32_t flagsOffset;                /* 0x050 */
    uint32_t varsOffset;                 /* 0x054 */
    uint32_t pokedexOffset;              /* 0x058 */
    uint32_t seen1Offset;                /* 0x05C */
    uint32_t seen2Offset;                /* 0x060 */
    uint32_t pokedexVar;                 /* 0x064 */
    uint32_t pokedexFlag;                /* 0x068 */
    uint32_t mysteryGiftFlag;            /* 0x06C */
    uint32_t pokedexCount;               /* 0x070 */
    uint8_t playerNameLength;            /* 0x074 */
    uint8_t field_075;                   /* 0x075 */
    uint8_t pokemonNameLength1;          /* 0x076 */
    uint8_t pokemonNameLength2;          /* 0x077 */
    uint8_t field_078;                   /* 0x078 */
    uint8_t field_079;                   /* 0x079 */
    uint8_t field_07A;                   /* 0x07A */
    uint8_t field_07B;                   /* 0x07B */
    uint8_t field_07C;                   /* 0x07C */
    uint8_t field_07D;                   /* 0x07D */
    uint8_t field_07E;                   /* 0x07E */
    uint8_t field_07F;                   /* 0x07F */
    uint8_t field_080;                   /* 0x080 */
    uint8_t field_081;                   /* 0x081 */
    uint8_t field_082;                   /* 0x082 */
    uint8_t field_083;                   /* 0x083 */
    uint8_t field_084;                   /* 0x084 */
    uint8_t padding_085[3];              /* 0x085 */
    uint32_t saveBlock2Size;             /* 0x088 */
    uint32_t saveBlock1Size;             /* 0x08C */
    uint32_t partyCountOffset;           /* 0x090 */
    uint32_t partyOffset;                /* 0x094 */
    uint32_t warpFlagsOffset;            /* 0x098 */
    uint32_t trainerIdOffset;            /* 0x09C */
    uint32_t playerNameOffset;           /* 0x0A0 */
    uint32_t playerGenderOffset;         /* 0x0A4 */
    uint32_t field_0A8;                  /* 0x0A8 */
    uint32_t field_0AC;                  /* 0x0AC */
    uint32_t externalEventFlagsOffset;   /* 0x0B0 */
    uint32_t externalEventDataOffset;    /* 0x0B4 */
    uint32_t field_0B8;                  /* 0x0B8 */
    uint32_t speciesInfo;                /* 0x0BC */
    uint32_t abilityNames;               /* 0x0C0 */
    uint32_t abilityDescriptions;        /* 0x0C4 */
    uint32_t items;                      /* 0x0C8 */
    uint32_t moves;                      /* 0x0CC */
    uint32_t ballGfx;                    /* 0x0D0 */
    uint32_t ballPalettes;               /* 0x0D4 */
    uint32_t gcnLinkFlagsOffset;         /* 0x0D8 */
    uint32_t gameClearFlag;              /* 0x0DC */
    uint32_t ribbonFlag;                 /* 0x0E0 */
    uint8_t bagCountItems;               /* 0x0E4 */
    uint8_t bagCountKeyItems;            /* 0x0E5 */
    uint8_t bagCountPokeballs;           /* 0x0E6 */
    uint8_t bagCountTMHMs;               /* 0x0E7 */
    uint8_t bagCountBerries;             /* 0x0E8 */
    uint8_t pcItemsCount;                /* 0x0E9 */
    uint8_t padding_0EA[2];              /* 0x0EA */
    uint32_t pcItemsOffset;               /* 0x0EC */
    uint32_t giftRibbonsOffset;          /* 0x0F0 */
    uint32_t enigmaBerryOffset;          /* 0x0F4 */
    uint32_t enigmaBerrySize;            /* 0x0F8 */
    uint32_t moveDescriptions;           /* 0x0FC */
    uint32_t field_100;                  /* 0x100 */
};

_Static_assert(sizeof(struct GfRomHeader) == 0x104, "GfRomHeader must be 0x104 bytes");

#endif /* GUARD_GF_ROM_HEADER_H */

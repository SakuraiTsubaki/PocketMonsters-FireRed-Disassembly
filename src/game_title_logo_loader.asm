; Verified CB2_InitTitleScreen state-1 game-title logo tile request.
; Per-ROM offsets are recorded in analysis/*-game-title-logo-load.json.

LoadGameTitleLogoTiles::
    ldr r1, =GameTitleLogoTiles
    movs r4, #0
    str r4, [sp]
    movs r0, #0
    movs r2, #0
    movs r3, #0
    bl DecompressAndCopyTileDataToVram

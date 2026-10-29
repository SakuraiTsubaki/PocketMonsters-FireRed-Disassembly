.syntax unified
.thumb

InitMainCallbacks:
    push {r4, lr}
    ldr r0, =gMain
    movs r4, #0
    str r4, [r0, #0x20]
    str r4, [r0, #0x24]
    str r4, [r0]
    ldr r0, =CB2_InitCopyrightScreenAfterBootup
    bl SetMainCallback2
    ldr r0, =gSaveBlock2Ptr
    ldr r1, =gSaveBlock2
    str r1, [r0]
    ldr r2, =gSaveBlock1Ptr
    ldr r0, =gSaveBlock1
    str r0, [r2]
    ldr r1, =gSaveBlock2
    movs r0, #0xF2
    lsls r0, r0, #4
    adds r1, r1, r0
    str r4, [r1]
    ldr r0, =gQuestLogPlaybackState
    strb r4, [r0]
    pop {r4}
    pop {r0}
    bx r0

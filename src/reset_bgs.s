.syntax unified
.thumb

.equ REG_BASE_MINUS_0x10, 0x03FFFFF0

ResetBgs:
    push {lr}
    bl ResetBgControlStructs
    ldr r1, =sGpuBgConfigs
    movs r0, #0
    strh r0, [r1, #0x10]
    bl SetTextModeAndHideBgs
    pop {r0}
    bx r0

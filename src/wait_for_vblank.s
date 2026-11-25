.syntax unified
.thumb

.global WaitForVBlank
.type WaitForVBlank, %function
WaitForVBlank:
    push {lr}
    ldr r2, =gMain
    ldrh r1, [r2, #28]
    ldr r0, =0x0000FFFE
    ands r0, r1
    strh r0, [r2, #28]
.LWaitSet:
    ldrh r1, [r2, #28]
    movs r0, #1
    ands r0, r1
    cmp r0, #0
    beq .LWaitSet
.LWaitClear:
    ldrh r1, [r2, #28]
    movs r3, #1
    adds r0, r3, #0
    ands r0, r1
    cmp r0, #0
    bne .LWaitClear
    pop {r0}
    bx r0
.size WaitForVBlank, . - WaitForVBlank

.syntax unified
.thumb

.global EnableVCountIntrAtLine150
.type EnableVCountIntrAtLine150, %function
.thumb_func
EnableVCountIntrAtLine150:
    push {lr}
    movs r0, #4
    bl GetGpuReg
    movs r1, #0xff
    ands r1, r0
    movs r2, #150
    lsls r2, r2, #8
    adds r0, r2, #0
    orrs r1, r0
    movs r0, #0x20
    orrs r1, r0
    movs r0, #4
    bl SetGpuReg
    movs r0, #4
    bl EnableInterrupts
    pop {r0}
    bx r0
.size EnableVCountIntrAtLine150, . - EnableVCountIntrAtLine150

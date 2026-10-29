.syntax unified
.thumb

ClearDma3Requests:
    push {lr}
    ldr r2, =sDma3ManagerLocked
    movs r0, #1
    strb r0, [r2]
    ldr r1, =sDma3RequestCursor
    movs r0, #0
    strb r0, [r1]
    movs r3, #0
    ldr r0, =sDma3Requests
    movs r1, #0x7f
request_loop:
    strh r3, [r0, #8]
    str r3, [r0]
    str r3, [r0, #4]
    adds r0, #0x10
    subs r1, #1
    cmp r1, #0
    bge request_loop
    movs r0, #0
    strb r0, [r2]
    pop {r0}
    bx r0


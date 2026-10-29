.syntax unified
.thumb

InitHeap:
    push {lr}
    ldr r2, =sHeapStart
    str r0, [r2]
    ldr r2, =sHeapSize
    str r1, [r2]
    bl PutFirstMemBlockHeader
    pop {r0}
    bx r0


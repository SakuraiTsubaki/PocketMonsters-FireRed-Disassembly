.syntax unified
.thumb

SetDefaultFontsPointer:
    push {lr}
    ldr r0, =gFontInfos
    bl SetFontsPointer
    pop {r0}
    bx r0


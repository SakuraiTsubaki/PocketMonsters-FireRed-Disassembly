.syntax unified
.arm
.section .text.rom_bootstrap, "ax", %progbits
.global rom_bootstrap
rom_bootstrap:
    .word 0xe3a00012 @ 0x08000204 other
    .word 0xe129f000 @ 0x08000208 other
    .word 0xe59fd028 @ 0x0800020c ldr-literal
    .word 0xe3a0001f @ 0x08000210 other
    .word 0xe129f000 @ 0x08000214 other
    .word 0xe59fd018 @ 0x08000218 ldr-literal
    .word 0xe59f101c @ 0x0800021c ldr-literal
    .word 0xe28f0020 @ 0x08000220 other
    .word 0xe5810000 @ 0x08000224 other
    .word 0xe59f1014 @ 0x08000228 ldr-literal
    .word 0xe1a0e00f @ 0x0800022c other
    .word 0xe12fff11 @ 0x08000230 bx


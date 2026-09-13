/*
 * FireRed ARM startup and IRQ dispatcher.
 *
 * Verified byte-exact against all eight project baselines at
 * ROM 0x000204..0x0003A3. The instruction stream is common to every
 * language/revision; only the linker-resolved gSTWIStatus and gIntrTable
 * literal values differ between builds.
 */

.syntax unified
.arm

.equ PSR_IRQ_MODE,        0x12
.equ PSR_SYS_MODE,        0x1F
.equ PSR_I_BIT,           0x80
.equ PSR_F_BIT,           0x40
.equ PSR_MODE_MASK,       0x1F

.equ IWRAM_END,           0x03008000
.equ INTR_VECTOR,         0x03007FFC

.equ REG_BASE,            0x04000000
.equ OFFSET_REG_IE,       0x0200
.equ REG_IF_MINUS_IE,     0x0002
.equ REG_IME_MINUS_IE,    0x0008
.equ REG_SOUNDCNT_X_MINUS_IE, -0x017C

.equ INTR_FLAG_VBLANK,    0x0001
.equ INTR_FLAG_HBLANK,    0x0002
.equ INTR_FLAG_VCOUNT,    0x0004
.equ INTR_FLAG_TIMER0,    0x0008
.equ INTR_FLAG_TIMER1,    0x0010
.equ INTR_FLAG_TIMER2,    0x0020
.equ INTR_FLAG_TIMER3,    0x0040
.equ INTR_FLAG_SERIAL,    0x0080
.equ INTR_FLAG_DMA0,      0x0100
.equ INTR_FLAG_DMA1,      0x0200
.equ INTR_FLAG_DMA2,      0x0400
.equ INTR_FLAG_DMA3,      0x0800
.equ INTR_FLAG_KEYPAD,    0x1000
.equ INTR_FLAG_GAMEPAK,   0x2000

.extern AgbMain
.extern gSTWIStatus
.extern gIntrTable

.align 2, 0
.global start_vector
start_vector:
    mov r0, #PSR_IRQ_MODE
    msr cpsr_cf, r0
    ldr sp, sp_irq
    mov r0, #PSR_SYS_MODE
    msr cpsr_cf, r0
    ldr sp, sp_usr
    ldr r1, =INTR_VECTOR
    adr r0, intr_main
    str r0, [r1]
    ldr r1, =AgbMain
    mov lr, pc
    bx r1
    b start_vector

.align 2, 0
sp_usr:
    .word IWRAM_END - 0x1C0
sp_irq:
    .word IWRAM_END - 0x60

.pool

.arm
.align 2, 0
.global intr_main
intr_main:
    mov r3, #REG_BASE
    add r3, r3, #OFFSET_REG_IE
    ldr r2, [r3]
    ldrh r1, [r3, #REG_IME_MINUS_IE]
    mrs r0, spsr
    stmdb sp!, {r0-r3, lr}
    mov r0, #0
    strh r0, [r3, #REG_IME_MINUS_IE]
    and r1, r2, r2, lsr #16
    mov r12, #0

    ands r0, r1, #INTR_FLAG_VCOUNT
    bne jump_intr
    add r12, r12, #4
    mov r0, #1
    strh r0, [r3, #REG_IME_MINUS_IE]

    ands r0, r1, #INTR_FLAG_SERIAL
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_TIMER3
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_HBLANK
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_VBLANK
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_TIMER0
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_TIMER1
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_TIMER2
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_DMA0
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_DMA1
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_DMA2
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_DMA3
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_KEYPAD
    bne jump_intr
    add r12, r12, #4
    ands r0, r1, #INTR_FLAG_GAMEPAK
    strbne r0, [r3, #REG_SOUNDCNT_X_MINUS_IE]

.Lirq_spin:
    bne .Lirq_spin

jump_intr:
    strh r0, [r3, #REG_IF_MINUS_IE]
    bic r2, r2, r0
    ldr r0, =gSTWIStatus
    ldr r0, [r0]
    ldrb r0, [r0, #0xA]
    mov r1, #INTR_FLAG_TIMER0
    lsl r0, r1, r0
    orr r0, r0, #INTR_FLAG_GAMEPAK
    orr r1, r0, #(INTR_FLAG_SERIAL | INTR_FLAG_TIMER3 | INTR_FLAG_VCOUNT | INTR_FLAG_HBLANK)
    and r1, r1, r2
    strh r1, [r3]

    mrs r3, cpsr
    bic r3, r3, #(PSR_I_BIT | PSR_F_BIT | PSR_MODE_MASK)
    orr r3, r3, #PSR_SYS_MODE
    msr cpsr_cf, r3

    ldr r1, =gIntrTable
    add r1, r1, r12
    ldr r0, [r1]
    stmdb sp!, {lr}
    adr lr, intr_return
    bx r0

intr_return:
    ldmia sp!, {lr}
    mrs r3, cpsr
    bic r3, r3, #(PSR_I_BIT | PSR_F_BIT | PSR_MODE_MASK)
    orr r3, r3, #(PSR_I_BIT | PSR_IRQ_MODE)
    msr cpsr_cf, r3
    ldmia sp!, {r0-r3, lr}
    strh r2, [r3]
    strh r1, [r3, #REG_IME_MINUS_IE]
    msr spsr_cf, r0
    bx lr

.pool
.align 2, 0

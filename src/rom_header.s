/*
 * FireRed GBA ROM header source.
 *
 * The standard Nintendo logo/title/game-code/checksum fields are populated by
 * tools/fix_gba_header.py after linking. The source-owned bytes at 0xC0..0xFF
 * are identical across all eight verified FireRed baselines.
 */

.syntax unified
.arm

.extern start_vector

.global Start
Start:
    b start_vector

.global RomHeaderNintendoLogo
RomHeaderNintendoLogo:
    .space 156

.global RomHeaderGameTitle
RomHeaderGameTitle:
    .space 12

.global RomHeaderGameCode
RomHeaderGameCode:
    .space 4

.global RomHeaderMakerCode
RomHeaderMakerCode:
    .space 2

.global RomHeaderMagic
RomHeaderMagic:
    .byte 0

.global RomHeaderMainUnitCode
RomHeaderMainUnitCode:
    .byte 0

.global RomHeaderDeviceType
RomHeaderDeviceType:
    .byte 0

.global RomHeaderReserved1
RomHeaderReserved1:
    .space 7

.global RomHeaderSoftwareVersion
RomHeaderSoftwareVersion:
    .byte 0

.global RomHeaderChecksum
RomHeaderChecksum:
    .byte 0

.global RomHeaderReserved2
RomHeaderReserved2:
    .space 2

/* 0xC0..0xFF: GPIO mirrors and fixed erased padding. */
    .word 0

.global GPIOPortData
GPIOPortData:
    .hword 0

.global GPIOPortDirection
GPIOPortDirection:
    .hword 0

.global GPIOPortReadEnable
GPIOPortReadEnable:
    .hword 0

    .space 6

    .rept 12
    .word 0xFFFFFFFF
    .endr

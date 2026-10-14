; BPRJ rev0 species 410 (Deoxys, Attack Forme) table evidence.
; Struct layout: data pointer, u16 size, u16 species tag.

gMonFrontPicTable = 0x081F4690
gMonBackPicTable  = 0x081F5B30
gMonPaletteTable  = 0x081F68F0

gMonFrontPicTable_Deoxys: ; ROM 0x001F5360
    .4byte 0x08D3958C
    .2byte 0x0800
    .2byte 0x019A

gMonBackPicTable_Deoxys: ; ROM 0x001F6800
    .4byte 0x08D39D70
    .2byte 0x0800
    .2byte 0x019A

gMonPaletteTable_Deoxys: ; ROM 0x001F75C0
    .4byte 0x08D39D48
    .2byte 0x019A
    .2byte 0

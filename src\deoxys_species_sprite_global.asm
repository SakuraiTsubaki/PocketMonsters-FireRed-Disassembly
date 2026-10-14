; Global rev0 species 410 (Deoxys, Attack Forme) table evidence.
; Struct layout: data pointer, u16 size, u16 species tag.

; language  front table  front entry  front data  back table  back entry  back data  palette data
; English   0x082350AC   0x08235D7C   0x08E3958C  0x0823654C  0x0823721C  0x08E39D70 0x08E39D48
; German    0x08234F7C   0x08235C4C   0x08E39580  0x0823641C  0x082370EC  0x08E39D64 0x08E39D3C
; French    0x0822F4B8   0x08230188   0x08E3958C  0x08230958  0x08231628  0x08E39D70 0x08E39D48
; Italian   0x0822E150   0x0822EE20   0x08E39584  0x0822F5F0  0x082302C0  0x08E39D68 0x08E39D40
; Spanish   0x08230818   0x082314E8   0x08E3958C  0x08231CB8  0x08232988  0x08E39D70 0x08E39D48

; Every listed species entry has size 0x0800 and tag 0x019A.
; The decoded front, back, and palette payloads are identical across these
; five releases even where their compressed streams begin at different offsets.

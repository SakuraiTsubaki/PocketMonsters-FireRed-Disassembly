.syntax unified
.thumb

.global VBlankIntr
.type VBlankIntr, %function
VBlankIntr:
    @ Synchronize link/wireless state according to the release profile.
    @ Advance the verified gMain VBlank counters and invoke its callback.
    @ Flush buffered video/DMA state where present, service sound/link data,
    @ advance RNG under the profile guard, then set bit 0 in both interrupt flags.
    bl RfuVSync
    bl LinkVSync
    bl CallVBlankCallback
    bl CopyBufferedValuesToGpuRegs
    bl ProcessDma3Requests
    bl m4aSoundMain
    bl TryReceiveLinkBattleData
    bl Random
    bl UpdateWirelessStatusIndicatorSprite
    bx lr
.size VBlankIntr, . - VBlankIntr

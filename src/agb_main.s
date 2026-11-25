.syntax unified
.thumb

.global AgbMain

.type AgbMain, %function
AgbMain:
    @ Structural reconstruction; per-release maps preserve conditional edges.
    bl RegisterRamReset
    bl InitGpuRegManager
    bl InitKeys
    bl InitIntrHandlers
    bl m4aSoundInit
    bl EnableVCountIntrAtLine150
    bl InitRFU
    bl CheckForFlashMemory
    bl InitMainCallbacks
    bl InitMapMusic
    bl ClearDma3Requests
    bl ResetBgs
    bl InitHeap
    bl SetDefaultFontsPointer
    bl SetNotInSaveFailedScreen
    bl AGBPrintInit
    bl ReadKeys
    bl rfu_REQ_stopMode
    bl rfu_waitREQComplete
    bl DoSoftReset
    bl Overworld_SendKeysToLinkIsRunning
    bl UpdateLinkAndCallCallbacks
    bl UpdateLinkAndCallCallbacks
    bl Overworld_RecvKeysFromLinkIsRunning
    bl ClearSpriteCopyRequests
    bl UpdateLinkAndCallCallbacks
    bl PlayTimeCounter_Update
    bl MapMusicMain
    bl WaitForVBlank
.Lagb_print_loop:
    b .Lagb_print_loop
.size AgbMain, . - AgbMain

.type AgbMain_no_agb_print, %function
AgbMain_no_agb_print:
    @ Structural reconstruction; per-release maps preserve conditional edges.
    bl RegisterRamReset
    bl InitGpuRegManager
    bl InitKeys
    bl InitIntrHandlers
    bl m4aSoundInit
    bl EnableVCountIntrAtLine150
    bl InitRFU
    bl CheckForFlashMemory
    bl InitMainCallbacks
    bl InitMapMusic
    bl ClearDma3Requests
    bl ResetBgs
    bl InitHeap
    bl SetDefaultFontsPointer
    bl SetNotInSaveFailedScreen
    bl ReadKeys
    bl rfu_REQ_stopMode
    bl rfu_waitREQComplete
    bl DoSoftReset
    bl Overworld_SendKeysToLinkIsRunning
    bl UpdateLinkAndCallCallbacks
    bl UpdateLinkAndCallCallbacks
    bl Overworld_RecvKeysFromLinkIsRunning
    bl ClearSpriteCopyRequests
    bl UpdateLinkAndCallCallbacks
    bl PlayTimeCounter_Update
    bl MapMusicMain
    bl WaitForVBlank
.Lno_agb_print_loop:
    b .Lno_agb_print_loop
.size AgbMain_no_agb_print, . - AgbMain_no_agb_print

.type AgbMain_agb_print_flash_fallback, %function
AgbMain_agb_print_flash_fallback:
    @ Structural reconstruction; per-release maps preserve conditional edges.
    bl RegisterRamReset
    bl InitGpuRegManager
    bl InitKeys
    bl InitIntrHandlers
    bl m4aSoundInit
    bl EnableVCountIntrAtLine150
    bl InitRFU
    bl CheckForFlashMemory
    bl InitMainCallbacks
    bl InitMapMusic
    bl ClearDma3Requests
    bl ResetBgs
    bl InitHeap
    bl SetDefaultFontsPointer
    bl SetNotInSaveFailedScreen
    bl AGBPrintInit
    bl SetMainCallback2
    bl ReadKeys
    bl rfu_REQ_stopMode
    bl rfu_waitREQComplete
    bl DoSoftReset
    bl Overworld_SendKeysToLinkIsRunning
    bl UpdateLinkAndCallCallbacks
    bl UpdateLinkAndCallCallbacks
    bl Overworld_RecvKeysFromLinkIsRunning
    bl ClearSpriteCopyRequests
    bl UpdateLinkAndCallCallbacks
    bl PlayTimeCounter_Update
    bl MapMusicMain
    bl WaitForVBlank
.Lagb_print_flash_fallback_loop:
    b .Lagb_print_flash_fallback_loop
.size AgbMain_agb_print_flash_fallback, . - AgbMain_agb_print_flash_fallback

.type AgbMain_flash_fallback, %function
AgbMain_flash_fallback:
    @ Structural reconstruction; per-release maps preserve conditional edges.
    bl RegisterRamReset
    bl InitGpuRegManager
    bl InitKeys
    bl InitIntrHandlers
    bl m4aSoundInit
    bl EnableVCountIntrAtLine150
    bl InitRFU
    bl CheckForFlashMemory
    bl InitMainCallbacks
    bl InitMapMusic
    bl ClearDma3Requests
    bl ResetBgs
    bl InitHeap
    bl SetDefaultFontsPointer
    bl SetNotInSaveFailedScreen
    bl SetMainCallback2
    bl ReadKeys
    bl rfu_REQ_stopMode
    bl rfu_waitREQComplete
    bl DoSoftReset
    bl Overworld_SendKeysToLinkIsRunning
    bl UpdateLinkAndCallCallbacks
    bl UpdateLinkAndCallCallbacks
    bl Overworld_RecvKeysFromLinkIsRunning
    bl ClearSpriteCopyRequests
    bl UpdateLinkAndCallCallbacks
    bl PlayTimeCounter_Update
    bl MapMusicMain
    bl WaitForVBlank
.Lflash_fallback_loop:
    b .Lflash_fallback_loop
.size AgbMain_flash_fallback, . - AgbMain_flash_fallback

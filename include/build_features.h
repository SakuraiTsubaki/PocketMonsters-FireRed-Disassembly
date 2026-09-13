#ifndef GUARD_BUILD_FEATURES_H
#define GUARD_BUILD_FEATURES_H

/*
 * Per-baseline behavior verified directly against the eight FireRed ROMs.
 * Values are supplied by config/targets.mk. Do not infer these from
 * GAME_REVISION alone: regional builds with the same software version differ.
 */

#ifndef FEATURE_PRINT_INIT
#error "FEATURE_PRINT_INIT must be provided by the selected FireRed target"
#endif

#ifndef FEATURE_FLASH_MEMORY_GUARD
#error "FEATURE_FLASH_MEMORY_GUARD must be provided by the selected FireRed target"
#endif

#ifndef FEATURE_ASSERTS_ENABLED
#error "FEATURE_ASSERTS_ENABLED must be provided by the selected FireRed target"
#endif

#if (FEATURE_PRINT_INIT != 0) && (FEATURE_PRINT_INIT != 1)
#error "FEATURE_PRINT_INIT must be 0 or 1"
#endif

#if (FEATURE_FLASH_MEMORY_GUARD != 0) && (FEATURE_FLASH_MEMORY_GUARD != 1)
#error "FEATURE_FLASH_MEMORY_GUARD must be 0 or 1"
#endif

#if (FEATURE_ASSERTS_ENABLED != 0) && (FEATURE_ASSERTS_ENABLED != 1)
#error "FEATURE_ASSERTS_ENABLED must be 0 or 1"
#endif

#endif /* GUARD_BUILD_FEATURES_H */

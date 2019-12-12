/**
 * This class provides log wrappers for the classic system signals.
 */
#include <stdio.h>
#include "Logger.h"


void log_success() {
    printf("----------------------------------------------------\n");
    printf("All tests passed!\n");
    printf("Good Job!\n");
    printf("----------------------------------------------------\n");
}

void log_test(int user, int n) {
    printf("{{ targetMethod }}(%d): %d\n", n, user);
}

void log_no_match(int expected) {
    printf("==> Expected: %d\n", expected);
    printf("It does not match, not expected result.\n");
    printf("----------------------------------------------------\n");
}
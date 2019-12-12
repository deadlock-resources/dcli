#include <stdio.h>
#include <string.h>
#include "Target.h"
#include "Logger.h"


int main(int argc, char *argv[]) {
    // user result
    if (strcmp(argv[1], "Solve") == 0) {
        // User clicked on `Submit` button, we must verify it code.
        printf("Running tests..\n");
        // Simple tests to verify user entry.

        {{ targetMethod }}(/* //TODO args to supply to test user code */)

        //TODO then if everything went well you can log it
        log_success();

        //TODO if something bad happened you have to return 1
        //you can also log something 
    } else {
        // User clicked on `Run` button
        printf("Running main method..\n");
        run();
    }

    return 0;
}
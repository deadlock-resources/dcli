#include <iostream>
#include "Target.h"
#include "Logger.h"
#include <cstring>

using namespace std;


{{ targetMethodReturn }} success_{{ targetMethod }}({{ targetMethodArgs }}) {
        //TODO write your own solution
        // You also have to implement it into success folder.
        return 1;
}


int main(int argc, char *argv[]) {
    try {
        // user result
        Target target = Target();
        {{ targetMethodReturn }} result = target.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});

        if (strcmp(argv[1], "Solve") == 0) {
            // User clicked on `Submit` button, we must verify it code.
            {{ targetMethodReturn }} expected = success_{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
            Logger::log(result, expected);
            if (expected == result) {
                Logger::log_success();
                return 0;
            } else {
                Logger::log_no_match();
                return 1;
            }
        }
    } catch (const std::exception& e) {
        Logger::log_exception(e);
        return 1;
    }
    return 0;
}

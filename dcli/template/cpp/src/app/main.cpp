#include <iostream>
#include "Target.h"
#include "Logger.h"
#include <cstring>

using namespace std;


{% if targetMethodReturn == "" %}void{% else %}{{ targetMethodReturn }}{% endif %} success_{{ targetMethod }}({{ targetMethodArgs }}) {
        //TODO write your own solution
        // You also have to implement it into success folder.
        {% if targetMethodReturn != "" %}return 1;{% endif %}
}

int main(int argc, char *argv[]) {
    try {
        // user result
        Target target = Target();
        
        {%if targetMethodReturn == "" %}
        // call user method without return
        //TODO do your own test, guess you are giving a pointer
        target.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
        {% else %}
        // store user result
        {{ targetMethodReturn }} result = target.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
        {% endif %}

        if (strcmp(argv[1], "Solve") == 0) {
            // User clicked on `Submit` button, we must verify it code.
            {%if targetMethodReturn == "" %}
            // call success method without return
            success_{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
            //TODO do your own test to verify the user method!
            {% else %}
            {{ targetMethodReturn }} expected = success_{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});

            Logger::log(result, expected);

            //TODO you have to do different tests to be sure user has the good solution.
            if (expected == result) {
                Logger::log_success();
                return 0;
            } else {
                Logger::log_no_match();
                return 1;
            }
            {% endif %}
        }
    } catch (const std::exception& e) {
        Logger::log_exception(e);
        return 1;
    }
    return 0;
}

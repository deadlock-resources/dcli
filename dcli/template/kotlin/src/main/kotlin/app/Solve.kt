package app

import template.{{ targetFile }}
import kotlin.system.exitProcess

/**
 * Class executed when user click on `Submit` button.
 * It must test if the user has reach or not the solution
 * with many tests.
 * Also have to exit(1) if something is wrong
 * And exit(0) if everything was fine.
 */
class Solve {
    companion object {
        fun main() {
            try {
                {%if targetMethodReturn == "" %}
                // call both method, user and success, do your own test to compare user code to the success one
                {{ targetFile }}.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
                success.{{ targetFile }}.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
                //TODO call Logger.logSuccess(); if everything is fine
                //TODO call exitProcess() is something went wrong and log it with Logger.logFail().
                {% else %}
                // user result
                val userResult = {{ targetFile }}.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
                // your solution result
                val expectedResult = success.{{ targetFile }}.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
                //TODO you have to do different tests to be sure user has the good solution.
                // comparing userResult and expectedResult

                if (expectedResult.equals(userResult)) {
                    // if all test passed successfully
                    Logger.logSuccess();
                } else {
                    Logger.logFail(expectedResult, userResult{% if targetMethodArgs != "" %}, /* //TODO fill it with your own args */{% endif %});
                    exitProcess(1);
                }
                {% endif %}
            } catch (e: RuntimeException) {
                Logger.logException(e);
                // if something bad happened exit with error code
                exitProcess(1);
            }
        }
    }

}

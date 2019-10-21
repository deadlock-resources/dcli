package app;

import template.{{ targetFile }};

/**
 * Class executed when user click on `Submit` button.
 * It must test if the user has reach or not the solution
 * with many tests.
 * Also have to exit(1) if something is wrong
 * And exit(0) if everything was fine.
 */
public class Solve {

    public static void main(String[] args) {
        try {
            // user result
            {{ targetMethodReturn }} userResult = {{ targetFile }}.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
            // your solution result
            {{ targetMethodReturn }} expectedResult = success.{{ targetFile }}.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
            //TODO you have to do different tests to be sure user has the good solution.
            // comparing userResult and expectedResult

            if (expectedResult.equals(userResult)) {
                // if all test passed successfully
                Logger.logSuccess();
            } else {
                Logger.logFail(expectedResult, userResult{% if targetMethodArgs != "" %}, /* //TODO fill it with your own args */{% endif %});
                System.exit(1);
            }
        } catch (RuntimeException e) {
            Logger.logException(e);
            // if something bad happened exit with error code
            System.exit(1);
        }
    }

}

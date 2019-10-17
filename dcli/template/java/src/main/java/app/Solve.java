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
            if ({{ targetFile }}.{{ targetMethod }} != success.{{ targetFile }}.{{ targetMethod }}) {
                // user result is not the same as expected
                // add more test to be sure user has well implementer the method.
                System.exit(1);
            }
            // all test passed successfully
            Logger.logSuccess();
        } catch (RuntimeException e) {
            Logger.logException(e);
            System.exit(1);
        }
    }

}

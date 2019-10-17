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
            // do some test with the user result
            {{ targetFile }}.{{ targetMethod }};
            // all test passed successfully
            Logger.logSuccess();
        } catch (RuntimeException e) {
            Logger.logException(e);
            System.exit(1);
        }
    }

}

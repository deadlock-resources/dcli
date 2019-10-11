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

        int min = 0;
        int max = 20;

        try {
            for (long n = min; n < max; n++) {
                // catching userValue
                long userValue = Fibonacci.fibonacci(n);
                long expectedValue = success.Fibonacci.fibonacci(n);
                if (expectedValue != userValue) {
                    Logger.logNoMatch(n, expectedValue, userValue);
                    System.exit(1);
                }
            }
            // all test passed successfully
            Logger.logSuccess();
        } catch (RuntimeException e) {
            Logger.logException(e);
            System.exit(1);
        }
    }

}

package app;

import template.{{ targetFile }};

/**
 * Class executed when user click on `Run` button.
 */
public class Run {

    public static void main(String[] args) {
        try {
            // just run user code
            {{ targetFile }}.main();
        } catch (RuntimeException e) {
            Logger.logException(e);
        }
    }

}

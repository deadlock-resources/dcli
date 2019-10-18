package app;

import template.{{ targetFile }};

public class Test {

    public static void main(String[] args) {
        try {
            // just run user code
            {{ targetFile }}.{{ targetMethod }}(/* //TODO fill it with your own args */);
        } catch (RuntimeException e) {
            Logger.logException(e);
        }
    }

}

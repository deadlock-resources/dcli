package app;

import template.Throug;

public class Test {

    public static void main(String[] args) {
        try {
            // just run user code
            Throug.main(/* //TODO fill it with your own args */);
        } catch (RuntimeException e) {
            Logger.logException(e);
        }
    }

}
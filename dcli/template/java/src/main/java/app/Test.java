package app;

import template.{{ targetFile }};

public class Test {

    public static void main(String[] args) {
        try {
            // just run user code
            {{ targetFile }}.{{ targetMethod }}({% if targetMethodArgs != "" %}/* //TODO fill it with your own args */{% endif %});
        } catch (RuntimeException e) {
            Logger.logException(e);
        }
    }

}

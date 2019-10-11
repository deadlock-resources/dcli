package app;

import template.{{ targetFile }};

public class Test {

    public static void main(String[] args) {
        try {
            {{ targetFile }}.{{ targetMethod }}({{ targetArgs }});
        }
        } catch (RuntimeException e) {
            Logger.logException(e);
        }
    }

}

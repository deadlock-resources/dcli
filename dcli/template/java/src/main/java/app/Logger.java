package app;

import java.util.Arrays;

/**
 * Simple logger class
 * You can use it to log useful information for the user.
 */
public class Logger {

    {%if targetMethodReturn == "" %}
    public static void logFail() {
        System.out.println("----------------------------------------------------");
        System.err.println("> {{ targetMethod }}() went wrong.");
        System.err.println("Try again.");
    }


    {% else %}
    public static void logFail({{ targetMethodReturn }} expected, {{ targetMethodReturn }} received) {
        System.out.println("----------------------------------------------------");
        System.err.println("> {{ targetMethod }}() = " + received);
        System.err.println("> Expected = " + expected);
        System.err.println("Received value is not correct.");
        System.err.println("Try again.");
    }

    public static void logFail({{ targetMethodReturn }} expected, {{ targetMethodReturn }} received, Object... input) {
        System.out.println("----------------------------------------------------");
        System.err.println("> {{ targetMethod }}(" + Arrays.toString(input) + ") = " + received);
        System.err.println("> Expected = " + expected);
        System.err.println("Received value is not correct.");
        System.err.println("Try again.");
    }
    {% endif %}

    public static void log(String message) {
        System.out.println("----------------------------------------------------");
        System.out.println(message);
        System.out.println("----------------------------------------------------");
    }

    public static void logSuccess() {
        System.out.println("----------------------------------------------------");
        System.out.println("Everything went well!");
        System.out.println("----------------------------------------------------");
    }

    public static void logException(Exception e) {
        System.err.println("----------------------------------------------------");
        System.err.println("An error occurred during runtime.");
        System.err.println("Details:");
        System.err.println(e.getMessage());
    }

    public static void logException(Throwable throwable) {
        System.err.println("----------------------------------------------------");
        System.err.println("Something bad happened!");
        System.err.println(throwable.getMessage());
        throwable.printStackTrace();
        System.err.println("----------------------------------------------------");
    }
}

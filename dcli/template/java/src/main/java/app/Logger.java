package app;

/**
 * Simple logger class
 * You can use it to log useful information for the user.
 */
public class Logger {

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

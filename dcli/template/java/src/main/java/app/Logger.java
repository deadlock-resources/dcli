package app;

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

    public static void logNoMatch(Long... args) {
        System.err.println("----------------------------------------------------");
        System.err.println("The result does not match the expected value for n = " + args[0]);
        System.err.println("expected: " + args[1]);
        System.err.println("your result: " + args[2]);
        System.err.println("----------------------------------------------------");
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

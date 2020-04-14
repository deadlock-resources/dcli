package app

import java.util.Arrays

/**
 * Simple logger class
 * You can use it to log useful information for the user.
 */
class Logger {
    companion object {
        {%if targetMethodReturn == "" %}
        fun logFail(): Unit {
            System.out.println("----------------------------------------------------");
            System.err.println("> {{ targetMethod }}() went wrong.");
            System.err.println("Try again.");
        }


        {% else %}
        fun logFail(expected: {{ targetMethodReturn }}, received: {{ targetMethodReturn }}): Unit {
            System.out.println("----------------------------------------------------");
            System.err.println("> {{ targetMethod }}() = " + received);
            System.err.println("> Expected = " + expected);
            System.err.println("Received value is not correct.");
            System.err.println("Try again.");
        }

        fun logFail(expected: {{ targetMethodReturn }}, received: {{ targetMethodReturn }}, vararg input: Any): Unit {
            System.out.println("----------------------------------------------------");
            System.err.println("> {{ targetMethod }}(" + Arrays.toString(input) + ") = " + received);
            System.err.println("> Expected = " + expected);
            System.err.println("Received value is not correct.");
            System.err.println("Try again.");
        }
        {% endif %}

        fun log(message: String): Unit {
            System.out.println("----------------------------------------------------");
            System.out.println(message);
            System.out.println("----------------------------------------------------");
        }

        fun logSuccess(): Unit {
            System.out.println("----------------------------------------------------");
            System.out.println("Everything went well!");
            System.out.println("----------------------------------------------------");
        }

        fun logException(e: Exception): Unit {
            System.err.println("----------------------------------------------------");
            System.err.println("An error occurred during runtime.");
            System.err.println("Details:");
            System.err.println(e.message);
        }

        fun logException(throwable: Throwable): Unit {
            System.err.println("----------------------------------------------------");
            System.err.println("Something bad happened!");
            System.err.println(throwable.message);
            throwable.printStackTrace();
            System.err.println("----------------------------------------------------");
        }
    }
}

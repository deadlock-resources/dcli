package app

fun main(vararg args: String) =
    if (args[0] == "Run") {
        Run.main()
    } else {
        Solve.main()
    }
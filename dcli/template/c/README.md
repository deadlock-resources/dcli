# What the sample contains
This sample contains a full implementation of a small C challenge.

The sample challenge is about **implementing Fibonacci**.

When the candidate will click on `Run` the `src/app/main.c` will be executed with the argument "Run", otherwise when user click 
on `Submit` the `src/app/main.c` will be executed with the `Solve` argument.

The first one should only run the candidate code, while the second one will verify if the candidat has the correct answer, comparing the success result to the template result mostly.


# Check-list
0. Set a beautifil thumbnail.png image for your challenge.
1. Modify the sample code in the **src/** directory to implement your own challenge
2. Update the template files within the **src/template** which will be sent to your candidates as a codebase
3. Update the success files provided to the candidate when the mission will be solved.
4. Change the **challenge.yaml** descriptor to match your challenge settings: description, xp, label, etc.
5. Update the docs **briefing**, **hint1**, and **hint2**. You can also provide translation under **fr/** for instance.


# Test your challenge with [Dcli](https://github.com/deadlock-resources/dcli):
```bash
#examples/code_c/ > dcli run
#examples/code_c/ > dcli solve
```


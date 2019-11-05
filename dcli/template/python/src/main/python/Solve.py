#
# File executed when user click on `Submit` button.
#  It must test if the user has reach or not the solution
#  with many tests.
#  Also have to sys.exit(1) if something is wrong
#  And sys.exit(0) if everything was fine.
# 
if __name__ == "__main__":
    import template
    import success
    import sys

    # Complete code with more test
    # Only one is not enough
    userValue = template.{{ targetMethod }}
    expectedValue = success.{{ targetMethod }}
    if userValue != expectedValue:
        print("Wrong value")
        print("> expected: " + str(expectedValue))
        print("> received: " + str(userValue))
        sys.exit(1)
    print("Good job!")

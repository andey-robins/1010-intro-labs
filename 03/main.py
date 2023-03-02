def is_even(n):
    return n % 2 == 0


def main():

    # these two lines handle getting the input to the program
    n = int(input())
    iterations = 0
    # please don't edit them, as the autograder uses them in this exact form

    # we will talk about this line later in class
    while n != 1:
        # don't worry about the above line until next week

        #############################
        #                           #
        # YOUR CODE GOES BELOW HERE #
        #      v     v     v        #
        #############################

        # TODO:
        # update the iterations variable so that it is now the value of iterations plus 1
        iterations = ???

        if is_even(n):
            # TODO:
            # call the appropriate collatz function below to update n
            n = ???
        else:
            # TODO:
            # call the appropriate collatz function below to update n
            n = ???

    # TODO:
    # call the print function with the argument `iterations`
    ???

# TODO:
# take the function described in the guide when a number is even and implement the correct
# collatz transformation in this function


def even_collatz(n):
    return ???


# TODO:
# write the function header for this function. it should take a single argument, named `n`
# you'll then call this function up in your if statement
???
return n * 3 + 1

main()

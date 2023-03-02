# Collatz Conjecture

# Collatz Conjecture

The Collatz Conjecture is a deceptively simple mathematics problem. It can be described as follows.

Assume you have some integer `n`.

 - If `n` is even, divide it by 2
 - If `n` is odd, multiply it by 3 and add 1

If you repeat this process until `n` is 1, it will always eventually transform into 1.


## Collatz Transformation

If we begin with `n = 6`, the Collatz transformation would be as follows:

 1. 6 is even, so divide by 2 and the result is 3.
 2. 3 is odd, so multiply by 3 and add 1. The result is 10
 3. 10 is even, so divide by 2 and the result is 5.
 4. 5 is odd, so multiply by 3 and add 1. The result is 16
 5. 16 is even, so divide by 2 and the result is 8
 6. 8 is even, so divide by 2 and the result is 4
 7. 4 is even, so divide by 2 and the result is 2
 8. 2 is even, so divide by 2 and the result is 1

In this example, we showed how the number 6 is a collatz number because by repeating the process it eventually turns into the number 1. For the above example, this took 8 steps.


## Lab

The Collatz Conjecture states that any integer eventually turns into 1 using these two rules, and is one of the most famous unsolved problems in mathematics.  

In lab today, we'll be writing a tool to count how many steps it takes to transform a number into a Collatz number.

The program will prompt you to input a number, so you can run and debug the entire program from the command line.

### Running and Testing

Use `python3 main.py` to start execution.

Then type in a number and press enter. If your code works correctly, inputting the numbers below in the table will yield the results in the table.

| Input | Output |
| ----- | ------ |
| 6     | 8      |
| 2     | 1      |
| 100   | 25     |
| 47    | 104    |
| 17    | 12     |

# Grading

## Grading

Grading will make use of an autograder. You may run it as many times as you like using the button below.

Furthermore, you may test the code yourself using the instructions on the previous page.

{Check It!|assessment}(code-output-compare-3263579208)


## Checklist

Complete the 5 TODO items within the `main.py` file. Each of these has instructions included in the `main.py` file which will describe how to complete the assignment.

If all of the checks pass above, you'll be all good to go!

## Submission

For this lab, you'll only need to proceed through the entire guide, ensure your code passes the test above on this page, and submit it through Codio. There is nothing that needs to be submitted on WyoCourses.

You may mark the assignment as completed in WyoCourses to avoid repeated notifications, but that is not required.
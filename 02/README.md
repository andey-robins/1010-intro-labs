# Welcome to Lab 2!

This lab will give you some hands on experience with programming using functions. Functions are a fundamental building block of code, so we'll be writing multiple of them. We'll also be calling these functions in order to build our application.

The application we're building today is a checkout application for a grocery store. Your code will be provided with the number of items being purchased, and it will then calculate the total cost of the visit to the grocery store.

## Learning Objectives

After this lab, students will be able to:

- fill out the body of a function from a description of the function;
- sequence functions in order to achieve a more complex task;
- and identify and fix a bug in a function.

## Tasks

The rest of the lab will walk you through all of the tasks needed to complete this application. Additionally, in the code file `checkout.py`, there are a number of places where I put the text `# TODO: ...` which provides a brief description of what needs done at that point as well as lets you know where changes will be necessary.

# Grading


## Grading

This page will run your code and evaluate its output to determine if your code is correct.

You'll receive one point for each test your code passes.

{Check It!|assessment}(code-output-compare-565624158)

## Inputs

Below I'm listing out the input values for your program. Use these to help you test your code! 

(You don't need to program them in anywhere specifically, the autograder takes care of all that for you :) )

|        | Peanut Butter | Jelly | Sourdough |
| ------ | ------------- | ----- | --------- |
| Test 1 | 1             | 2     | 3         |
| Test 2 | 5             | 3     | 2         |
| Test 3 | 2             | 7     | 11        |

## Submission

For this lab, you'll only need to proceed through the entire guide, ensure your code passes the test above on this page, and submit it through Codio. There is nothing that needs to be submitted on Wyocourses.

# Checkout Sum

## `checkout_sum()`

The `checkout_sum()` function is the function responsible for calculating the sum of three items. It takes three parameters, `price1`, `price2`, and `price3`. The first step of this lab is to finish that function.

The return value should be the sum of all three arguments. See some example invocations and return values below for more clarity.

### Example Function Calls

`checkout_sum(1, 2, 3)` returns `6`.

`checkout_sum(6, 4, 10)` returns `20`.

`checkout_sum(1.2, 2.2, 3.6)` returns `7.0`.

### Task

Implement the `checkout_sum()` function according to the description above. Check that it works by storing the result of the function in a variable and printing it to the console.

You can run your program manually by opening up a terminal under **Tools > Terminal** and then running the command `python3 checkout.py`


|||info
## Variables Hint
Reminder, storing a value into a variable will look something like this: `my_variable = my_function(1, 2, 3)`

Then you can print the value of `my_variable` by using the command `print(my_variable)`
|||

# Buy Many of Item

## `buy_many_of_item`

This function allows us to calculate the price for purchasing multiple of an item. It has two parameters, `item_price` and `number_of_items`. `item_price` is the cost for a single item. `number_of_items` is the number we're going to purchase.

For instance, if a gallon of milk costs $4.19 and we want to buy 2 gallons, the function would return 8.38. See below for more examples.

The return value should be the product of the two parameters.

### Example Function Calls

`buy_many_of_item(4.19, 2)` returns `8.38`
`buy_many_of_item(3, 3)` returns `9`
`buy_many_of_item(2.2, 5)` returns `11`

### Task

Implement the `buy_many_of_item()` function according to the description above. Check that it works by storing the result of the function in a variable and printing it to the console.

You can run your code from the terminal using the command `python3 checkout.py`

# Checkout Item

## `checkout_item`

This function has already been written by me; however, there is a bug in the code I wrote! First I'll describe what this function *should* do, and then your task will be to fix the function so it does what it's supposed to do.

`checkout_item()` is a function with two parameters, `subtotal` and `sales_tax`. The function returns the total price of the item *after* tax. 

|||info
## Tax in Laramie

This program assumes we're buying our items in Laramie, Wyoming. The sales tax here is 6%.
|||

### Example Function Calls

`checkout_item(100, 0.06)` returns `106`
`checkout_item(1.50, 0.06)` returns `1.59`
`checkout_item(11.50, 0.06)` returns `12.19`

### Task

If you run the example function calls provided above and print out the values, you'll see that they don't match the expected return values listed above. Your job is to fix the function so that it correctly returns the values listed above.

Some guidelines for how to accomplish this task:
1. Run the above examples and print out their return values. How are they different from the expected return values?
2. Look at the current function code. How are the return values being calculated?
3. Look at the examples above. How would you calculate the correct result given the inputs?
4. Take your answers to part 3 and implement them into the function. Print out the values after your changes. Does the function return the expected values?


|||important
## Hint

The total returned from the `checkout_item` function should be greater than the `subtotal` argument.
|||

Remember, you can put in print statements and run your code from the 'Grading' tab to check your work as you go.

# Calculate Prices

## Calculate the Prices for Items

We've now built each of the component parts of our application. Each of these are *encapsulated* or "contained" within a function. The next step is to sequence our functions in an order that turns our inputs into the outputs we want.

We'll go through this step by step in the coming guide pages.

### Sequencing our Calculations

1. Three variables have been created for you to hold the subtotal of each item. Use the `buy_many_of_item()` function along with the other variables in the program to calculate the cost of each item for the `..._count` and `..._cost` of each item.

2. Now that we have stored how much we will spend on each set of items, we need to calculate the totals for each item. Make use of one of the functions you edited during this lab to calculate the totals for each item.

# Sum Prices

## Sum All Prices

We've now calculated the total cost of each item we're purchasing.

The next step in our application is to sum all of the costs to get our grand total. 

1. Take the `..._total` variables for each item and calculate their sum
2. Store the result in the `total` variable

# Display Total

## Time for Output

1. There is a function in the `checkout.py` file that will output some "formatting text" to make your solution match the format expected by the autograder. Look through the file and identify the name of that function. 
2. Call that function with no arguments.
3. Finally, print the total you calculated in the previous step.

At this point, you have walked through each step of the process. Return to the grading tab and try running the whole thing! ()

## It Didn't Work....

That's alright! This is a fundamental part of computer science. When we run our programs they very rarely work perfectly the first time. The next step is to start debugging: figuring out what went wrong and why.

### Andey's Steps to debugging

1. **Take a deep breath.** Sometimes it's frustrating when you've been debugging for a long time. Don't be afraid to take a break, get up from the computer, and return to the problem after a few minutes. Sometimes a fresh pair of eyes can help get through the problem.
2. **Print out values as you go.** When you step through the lines in a program, you can expect a value to be something specific (often calculated by hand). Printing out the values can help find the place where your expectations and the program diverge.
3. **Remove pieces of the code.** You can use a `#` to comment that line of the program. This turns it into a piece of metadata that is ignored by the program. Commenting out lines that you know work, or you know aren't run yet, is a way to reduce the possibilities for what might be going wrong.
4. **Ask for help.** There's a technique in computer science called "pair programming" where two people work together to create code. As the saying goes, two heads really are better than one and sometimes it takes a different person's thought process to see what's going wrong.

## It Works!!

Congratulations!! You just wrote a functional cash register application! You've finished this lab and you can turn it in! Pat yourself on the back, because this was quite the undertaking. You may not have thought that just two weeks into this class you'd be writing applications, but you did it!
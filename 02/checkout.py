# this line of code allows me to access information
# about the system
import sys


def get_initial_item_counts():
    """
    Ignore this function for now. I've put it in to "hide away" the code
    that allows Codio to provide input to your program. I invoke this function
    on line number 62, so you can see how its used below.
    """
    return int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

# All of the code you will write is below this line
# -------------------------------------------------
# Everything above this line is code I wrote to make the autograder work
# I'm leaving it visible so you can see it isn't just magic! And by the
# end of the semester you'll be able to read and understand it all.


def buy_many_of_item(item_price, number_of_items):
    """
    This function calculates the total cost for multiple of an item.
    Imagine I want to calculate the cost of 4 bushels of bananas.
    I could provide the price of bananas as the argument `item_price`
    and I could provide the number of bananas as the argument `number_of_items`
    This function would then return the total cost of all four bushels of bananas
    """
    total = 0

    # TODO: You'll write this function!
    # Your code goes here :)

    return total


def checkout_item(subtotal, sales_tax):
    """
    This function takes the subtotal and the local sales tax as arguments
    It returns the total cost after tax
    """
    # TODO: You'll fix a bug here!
    return subtotal * sales_tax


def checkout_sum(price1, price2, price3):
    # TODO: You will implement this :)
    pass  # Delete this line after you start, it's here as a placeholder since otherwise
    # the function would be completely empty, and that's not allowed by python
    # don't forget to return your total when all the calculation is done!


def show_total_text():
    print('Your total is:', end=' ')

####################################
# THIS IS THE END OF THE FUNCTIONS #
# -------------------------------- #
# BELOW WILL BE YOUR SEQUENCE CODE #
####################################


# Don't change this line, it's getting the number of each item for your program!
peanut_butter_count, jelly_count, sourdough_count = get_initial_item_counts()

# These are the prices for each item.
# Please don't change them!
PEANUT_BUTTER_PRICE = 1.27
JELLY_PRICE = 4.97
SOURDOUGH_PRICE = 3.99

# Calculate the price for each set of items by
# calling a function you wrote
# TODO: Calculate these values :)
peanut_butter_subtotal = 0
jelly_subtotal = 0
sourdough_subtotal = 0

# Get the checkout cost for each item by calling
# one of the functions you wrote
# HINT: The sales tax in laramie is 6%
# TODO: Calculate these values :)
peanut_butter_total = 0
jelly_total = 0
sourdough_total = 0

# Calculate the total cost and print the cost
total = 0
# TODO: you'll need to do something here to make
# your output match what is expected :)
print(total)  # this line doesn't need any changes

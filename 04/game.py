# wizardry you'll learn later
import random
import time


def setup():
    random.seed(int(time.time()))


def computer_action():
    choice = random.randint(1, 3)
    if choice == 1:
        return "r"
    elif choice == 2:
        return "p"
    else:
        return "s"
# end wizardry

# TODO: Part of the IF statement has been removed, add it back in with
# the correct return value and boolean operator
# HINT: compare this to the other player_chose_whatever functions


def player_chose_rock(comp_choice):
    ???
       ???
    elif comp_choice == "p":
        return "computer"
    else:
        return "player"


# TODO: Write the function header for this function. The name of the
# function is somewhere else in this file
# HINT: maybe look for places where a function is called?
???
   if comp_choice == "p":
        return "draw"
    elif comp_choice == "s":
        return "computer"
    else:
        return "player"

# TODO: Fill in the return values so that the output matches the other functions
# You'll need to match up the boolean comparisons with the correct return values
# HINT: Look at player_chose_paper to see which three strings should be returned

def player_chose_scissors(comp_choice):
    if comp_choice == "s":
        return "???"
    elif comp_choice == "r":
        return "???"
    else:
        return "???"

# TODO: Complete this function by filling in the missing pieces
# You must correctly call a function, write a boolean expression, and return a value
# HINT: The three lines will look very similar, just calling different functions.

def find_winner(player_choice, comp_choice):
    if player_choice == "r":
        return ???(comp_choice)
    elif ???:
        return player_chose_paper(???)
    else:
        ???


def main():
    cont = True

    # TODO: Write a while loop that continues running until the player chooses to quit
    # HINT: look at what variables are available inside this function
    ???
       choice = input("[r]ock, [p]aper, [s]cissors? (q to quit)\n > ")

        if choice == "q":
            cont = False
        # TODO: Fill in the start of the other branch of the IF statement
        # so that this code only happens when choice is not equal to "q"
        # HINT: Brainstorm which types of IF statements we know
        ???
           computer_choice = computer_action()
            winner = find_winner(choice, computer_choice)

            print("The winner is: ", winner)


# please do not change these lines below
# if you do, the autograder will break :)
if __name__ == "__main__":
    setup()
    main()

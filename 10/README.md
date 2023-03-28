# Yacht

The dice game Yacht is a public domain dice game similar to Generala, Poker Dice, and Crag. It's perhaps best known for its modern, branded version Yahtzee® (Hasbro). [From Wikipedia](https://en.wikipedia.org/wiki/Yahtzee).

For this lab, I have written a game of Yacht and an AI for playing the game. However, I can't be bothered to debug the program and instead have turned to my lovely collection of newly minted programmers to ask their assistance. Each of the bugs in this program falls into one of three categories: syntax bugs; semantic bugs; and runtime bugs. These three categories are listed below. After you fix all of the bugs, the program will run, allowing you to play a game of Yacht if you like.

![Welcome to Debugging](Screenshot 2022-11-29 at 3.49.32 PM.png)

In the past, we may have viewed the interpreter as an adversary, someone we need to force into running our code. While it can sometimes feel this way, it would be more accurate to describe it as a very specific colleague. The interpreter will help you identify where your code is broken and what you need to do to fix it. Don't be afraid of the error messages; reading them in their entirety is often the best way to understand what is going wrong in the code.

## Types of Errors

### Syntax Bugs

These are some of the bugs we're most familiar with. This is something I know we've seen countless times: `SyntaxError: invalid syntax`. Using the information about where these bugs appear, track them down and fix them to get the program to actually run. After it begins running, you'll see more of the semantic bugs and logical bugs begin to appear.

### Semantic Bugs

Semantic bugs occur when we try to do something that isn't allowed by the language. Some common examples we've run into could be: using a list to index another list; calling a variable not a function; or giving the wrong type of values to a function. These may be a little trickier to find, so go through and work to identify what the values of variables should be and what they actually are. Use print statements liberally here to make your life easier! Since these won't appear unless you're running the program, I've also marked them as `# TODO` to make locating, but not necessarily fixing, them easier.

### Runtime Bugs

Runtime bugs or logical bugs are the most difficult to find since often the only symptom of them is that the program isn't doing what we expect it to do, but it doesn't crash or fail to tell us why. The best way to work on tracking these down is to work on identifying code that could potentially be run during the actions that we observe the bad behavior in. Use print statements and comments to keep track of your thoughts as you work through the code to identify these tricky bugs.

## Rubric

 - 1 point for fixing all of the syntax bugs
 - 2 points for fixing all of the semantic bugs
 - 1 point EC for fixing the logic bug *(Hint: it's something wrong with the AI)*
 - **Note: No partial credit on this one, getting it running is the way to get points :)**

## Tasks

1. Fix up my program :)
  - There are 8 syntax bugs, 4 semantic bugs, and 1 logical bug for you to track down.

## Grader

|||topic
## Open Your Code

[Open the code file](open_file student_code/yacht.py panel=2)

|||

|||topic
## Run your code by hand to play

`python3 student_code/yacht.py`

|||

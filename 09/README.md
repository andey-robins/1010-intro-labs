# Movies III

For lab today, we'll be once again extending our code from the last two weeks! So step one today is to go get your lab code from last week and put those functions into the code here. As a friendly reminder, that's a function called `frequent_words` which takes a single argument (the lines of a script) and another function called `get_most_frequent` which takes a dictionary and returns the most common value in that dicitonary.

For this lab, we'll be analyzing our data and generating some interesting graphics about the data using the modules we discussed in lecture this week. You'll be generating some frequency graphs to represent the most common words form different movies and visualize the ratio between them.

**Important note:** Don't worry about capitalization or any other string operations! For this, it's safe to assume I've already taken care of all of that for you :) All you need to use the strings for is maybe `split()`-ing them!

## Tasks
1. Add another argument to the `frequent_words` function so that the first argument is the name of the movie and the second argument is the script
2. Take the looping/top five code you wrote last week and put it in a function `get_top_n(freq_dict, n)` which takes an argument and returns the top *n* words and their frequencies
3. Transmute this data to a form that you can feed into matplotlib
4. Create a bar graph with the top 20 most frequent words from each movie

## Grader

|||topic
## Open Your Code

[Open the code file](open_file student_code/movies.py panel=2)

|||

**Run your code with the command `python3 grader.py` from the terminal!!**

## Installing matplotlib

```bash
sudo apt-get update
sudo apt-get install libjpeg-dev zlib1g-dev
pip3 install matplotlib
```
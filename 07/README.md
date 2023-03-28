# Movies I

```md
NOTE: scripts should be gathered from somewhere else. Names are provided in the grading script. 
```

For lab today, we'll be writing a piece of software that allows us to identify the most common words in movies. I've pre-populated a folder with a handful of example scripts that will be provided to your code by the autograder. 

**Important note:** Don't worry about capitalization or any other string operations! For this, it's safe to assume I've already taken care of all of that for you :) All you need to use the strings for is maybe `split()`-ing them!

## Tasks

1. Create a function called `frequent_words` which accepts a single argument, a list with the lines of the script contained as strings within the list.
2. Count the number of times each word appears in the script.
3. Identify the most common word in the script.
4. Return a list where the first item is the most common word and the second item is tAhe number of times the most frequent word was in the script. 

## Grader

|||topic
## Open Your Code

[Open the code file](open_file student_code/movies.py panel=2)

|||

{Check It!|assessment}(test-1176591700)

## Testing

I'm not providing any explicit code to test your code for you (note, the autograder will continue to give as good of feedback as it's able). Working out the way you think is best to test your code is an important skill to start developing!

Some things you can try:
1. Call your function at the end of the file with just a single string in a list, does it return the value you expect?
2. Write a short "script" and run it through your function, does it work?
3. Create some small examples you're able to run entirely on your own, does it work as you'd anticipate?
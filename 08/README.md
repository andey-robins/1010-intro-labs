# Movies II

For lab today, we'll be extending our code from last week! So step one today is to go get your lab code from last week and put that function into the code here. As a friendly reminder, that's a function called `frequent_words` which takes a single argument.

For this lab, we'll be continuing to process the data and getting slightly more meaningful output. The most common word we saw in the last lab was the word "the," which makes sense as it's one of the most common articles; however, we'd like to be able to find the most common "interesting" word. For the purposes of this lab, we'll define "interesting" as a word that isn't in this list:

```python
common_words = ['the', 'a', 'an', 'and', 'of', 'in', 'to', 'is', 'are', 'be', 'i', 'he', 'she', 'you', 'with', 'on', 'it', 'this', 'that', 'we', 'what', 'his', 'at', 'for', 'him', 'her', 'hers']
```

**Important note:** Don't worry about capitalization or any other string operations! For this, it's safe to assume I've already taken care of all of that for you :) All you need to use the strings for is maybe `split()`-ing them!

## Tasks

1. Remove all of the common words from our dictionary.
2. Create a function called `get_most_frequent(frequency_dict)` which returns the list from last lab.
    - Find the most frequent word and its count
    - return them in a list with the count followed by the word
3. Find the five most frequent, interesting words and return them in a list with the most common of them first and least common last.

## Grader

|||topic
## Open Your Code

[Open the code file](open_file student_code/movies.py panel=2)

|||

{Check It!|assessment}(test-1176591700)
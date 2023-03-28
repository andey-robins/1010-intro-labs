# Toki Pona

*toki! mi jan Andey.*

The above is my introduction in the lovely little language **toki pona**. It reads: "Hello! My name is Andey!" toki pona is a constructed language that was first published in 2001 by jan Sonja, a Canadian Linguist. 

In this lab, you'll be writing a bit of software that works as a translator from English to toki pona. You will create a function called `translate()` which takes an English sentence as an argument and returns the translated sentence in toki pona. 

To prevent you needing to learn the entire language (only 137 words), I've included an abridged dictionary of toki pona in the python dict `en2tp`. This allows for the lookup of English words, and the resulting value is that word translated into toki pona.

A collection of sentences and their translations are available for your convenience at the end of this guide. It's up to you to determine how to run your code using these as input, but you will make use of the command `python3 student_code/toki.py` to run your code file. 

**Note:** I have not put in any logic to run your code. If you want there to be output, you'll need to call your function and print the results with these sentences or something similar. Furthermore, if you add output statements here, you may need to delete them when you're sure your code works for the autograder to accept it.

## Tasks

1. Create a function named `translate` that accepts a sentence as the only argument.
2. Split the sentence into words. There will always be a single space between words. (i.e. `" "`)
3. Lookup the word in the dictionary `en2tp`. Please note, the word must be all lower case with no punctuation to be found in the dictionary.
4. Track the toki pona word for each English word, assembling them into a sentence in the same order they appear in the English sentence.
5. Return the translated sentence with proper capitalization and punctuation. (hint: toki pona doesn't capitalize words at the beginning of sentences.)

## Grader

|||topic
## Open Your Code

[Open the code file](open_file student_code/toki.py panel=2)

|||

{Check It!|assessment}(test-2574222899)


## Helpful Functions

Some of the following functions will be useful for dealing with strings.

|function|usage|example|result|
|--------|-----|-------|------|
|`split()`|`string.split(" ")`|`words = "Multiple words here".split(" ")`|`["Multiple", "words", "here"]`|
|`join()`|`string.join(list)`|`sentence = " ".join(["one", "word", "each])`|`"one word each"`|
|`lower()`|`string.lower()`|`whisper = "THIS IS SHOUTED".lower()`|`"this is shouted"`|
|list/string access|`string[4]`|`fourth_character = "hello"[4]`|`"o"`|
|dictionary access|`my_dictionary["word"]`|`good_tp = en2tp["good"]`|`"pona"`|
|concatenation|`string1 + string2`|`hello_world = "hello " + "world."`|`"hello world"`|

## toki pona sentences

|English|toki pona|
|-------|---------|
|Someone is good.|jan li pona.|
|They are sleeping.|oni li lape.|
|You are good.|sina li pona.|
|Love is good.|olin li pona.|
|My food is bad.|mi moku li ike.|
|I am your friend.|mi jan sina pona.|

## Want to learn more?

<iframe width="560" height="315" src="https://www.youtube.com/embed/2EZihKCB9iw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# Welcome to COSC 1010

I'm your intrepid GA for the course, Andey (They/Them). I'm a graduate students in Dr Borowczak's lab, and one of your points of contact for this course. See the syllabus for my office hours, email, and other ways to get in contact with me if you need! I look forward to guiding you on this journey into computer science.

Before we dive into the primary content for the lab, I have a few brief notes on style to share with you. Additionally, at the end of this page is a quick reference of all that needs to be turned in for the lab.

## Styling Conventions

I use `monospace text` to indicate code/something directly related to the machine.

**Bold** indicates either a path (such as file path or menu path) or a new term that should be highlighted.

*Italics* are used to indicate keywords that can be researched more for additional information now, or you can wait until the topic is introduced in more depth later on in the course.

Some links will appear, always styled as [LINK](https://wyoweb.uwyo.edu). This one links to Wyoweb. External links are always optional content unless otherwise is stated. They contain information that can enrich your understanding of the topic, though they are not required for this class.

Long sections of code will be presented in a code block like this:
```python
def main():
  for i in range(1, 10):
    print(i)
```
These blocks can be copied all at once by clicking the clipboard icon in the top left of the block on Codio.

Occasionally buttons will appear in Codio that perform some amount of action for you. In this lab for instance, you will encounter a button which runs your code for you (before we talk about how to run it manually). These will be blue buttons. Try clicking the one below.

{Buttons look like this}(echo 'You pressed the button')

# Learning Objectives

<br />
Throughout the course of this lab, you will learn about and develop a number of skills. They are enumerated below to guide you through this lab.
<br />

## Objectives
- Learn to create and run code on Codio
- Write your first python program
- Run your first program through Codio

# Submission

|||important
## Note

Future labs, homework, or quests *will* have to be submitted directly through the codio interface. 
Make sure to read directions carefully for each assignment.
|||

## Rubric
Labs are 3 points each and should align to:
| Points | Assessment            |
| ------ | --------------------- |
| 0      | No Attempt Made       |
| 1      | Insufficient Evidence |
| 2      | Partial Proficiency   |
| 3      | Proficient            |

## What to Turn In
As you go through this lab, you will take two screenshots. Instructions will be present throughout when you need to take a screenshot, but both of them are listed below as well.

1. A screenshot of your `main.py` file with an additional print statement.
2. The output of running `python3 main.py` on Codio


|||info
Upload these two images right here! Right click on the name of the assignment in the file tree and select the "Upload" option.
|||

# Your First Program

Let us now turn our attention from codio itself and begin the process of writing our first program.

## Hello World

Our first program will be a program that outputs a greeting of "hello world" to the terminal. Having your first program be a "hello world" program is a tradition almost as old as programming itself [\[LINK\]](https://dev.to/just5moreminutes/why-hello-world-5c0g), and one we'll keep alive here. Follow along with the instructions below to craft your program.

## Write The Program

1. In the filetree on the left hand side of your screen, click on the "root" of the directory. For this project, the root is titled "Hello World (master)" and has a lock icon to the left of it.

![The filetree](.guides/img/filetree.png)

2. Using the menu bar, create a new file with **File > New File**
3. In the popup, confirm that the text in the "current path" field says "root folder." If it says something else, repeat step 1.
4. In the "file name" field, type the name of the file: `main.py` 

![Creating the file](.guides/img/makefile.png)

5. The file should open and you will see a blank editor. If it doesn't open automatically, you can also click on the file `main.py` in the filetree on the left hand side of the screen.

![The newly created main file](.guides/img/openfile.png)
 
6. Type in the following code to your new, `main.py` file.

```python
print('Hello World!')
```

You've now written your first program. Click the next button below and learn how to run your program.

# Check Your Code

Click this button to see the output of your program.

{Run My Code}(python3 main.py)

Return to the `main.py` file and try outputting different text. Can you display multiple pieces of text? Can you change the text you wrote? Once you've played around with writing different code and re-running your code with the button above, return to this guide to learn how we run your code. Take a screenshot of your code after adding an additional print line.

## What is the button doing?

When you click the button above, it runs the following command:

```bash
python3 main.py
```

There are two parts to this command, and we'll explore them both now.

The first part of the command is `python3`. This text is the command that tells the computer which program we want to run. `python3` is telling the computer to run the python _interpreter_.

The second part of the command is `main.py`. This is called an argument. It is an additional piece of information that the running command makes use of. In this case, the program, `python3` uses the argument of `main.py` to know which file to run using `python3`.

Therefore, we can read the entire command as telling the computer to run the python interpreter on our file `main.py`

## Manually run commands

Now we're going to manually run our program.

1. Open up a terminal using **Tools > Terminal**

![The new terminal button](.guides/img/newterminal.png)

2. You will see a prompt like below in your terminal. Don't worry about everything you see. There's plenty to learn about the terminal and this interface, you'll probably pick up some tricks throughout this class, but we're just going to run our program for now.

![The new terminal](.guides/img/terminal.png)

3. Type the command `python3 main.py` into the terminal. Just like when you clicked the "RUN MY CODE" button above, this will run your program and output the results to the terminal.

![The results of our program](.guides/img/result.png)

If you added more output to your `main.py` program, you'll see that reflected in the output. I only have the single line of `print('Hello World!')` and so my output reflects that.

4. Take a screenshot of your terminal window with the output of your program.

## That's It!

At this point, upload your two images to Codio, and you'll be good to go for this first lab! There are two more pages of content in the lab, but they are purely optional. If you would like to learn about setting everything up on your computer instead of on Codio, they will walk you through that process. If you don't see the need for that right now, just know that everything we do can be done through Codio exclusively (and it's set up for Codio primarily too).

{Check It!|assessment}(code-output-compare-3386932572)

# [Optional] Your Equipment

|||warning
If you are planning to use your own computer for programming, there are a few steps to get yourself up and running. This is purely optional as between Codio and the Lab computers, we will ensure you have access to all the necessary resources for programming. However, if you want to set up the tools on your own computer, this will guide you through the process.
|||

If you run into troubles, come into office hours the first or second week of classes. I'll be happy to help walk you through installation processes during that time period. After the first two weeks, if you need help with installations, send me an email to see if I anticipate there being some spare time during office hours.

## Installing Python

The process is different for each different platform, so I'm unable to provide an entirely tailored guide here. Instead, I will link you to this outside tutorial [[LINK](https://realpython.com/installing-python/)]. As I mentioned previously, but bears repeating, there is no need for you to do this if you only plan on using the resources we provide to you. All of the necessary tools are made available to you automatically through Codio and on the University lab equipment. This is purely suplemental information.

# [Optional] Text Editors

*This text is copied from the previous Optional page*


|||warning
If you are planning to use your own computer for programming, there are a few steps to get yourself up and running. This is purely optional as between Codio and the Lab computers, we will ensure you have access to all the necessary resources for programming. However, if you want to set up the tools on your own computer, this will guide you through the process.
|||

If you run into troubles, come into office hours the first or second week of classes. I'll be happy to help walk you through installation processes during that time period. After the first two weeks, if you need help with installations, send me an email to see if I anticipate there being some spare time during office hours.

## Why Do I Need a Text Editor?

For this course, you don't! All of the work we're doing can be successfully done with Codio. Furthermore, if you absolutely *need* to program without an internet connection, the IDLE interpreter/editor is a capable enough tool for this class.

With that said, at some point in your computer science career, you'll reach the point where you want to have an editor of your own to configure and setup to fit your development workflow. Consider this page a brief discussion of common options to give you a jumping off point for this topic if that's what you're looking for.

## Notepad++

Notepad++ is a common first editor. Many folks begin their programming journey with Notepad++ and do plenty before even learning there's something more complex out there. Though it doesn't have the fancy features of other editors on this list, it will still get the job done.

Visit this page to get Notepad++ [[LINK](https://notepad-plus-plus.org)].

## VS Code

Since its release in 2015 VS Code has become the de facto standard for programming in most languages. The robust extension ecosystem means that whatever tool you need, there's likely an extension for VS Code to make that tool more easily accessible. 

Visit this page to get VS Code [[LINK](https://code.visualstudio.com)].

## Vim, Emacs, Nano, etc.

These editors are all used out of the command line. Their interfaces are almost entirely keyboard dependent, and the learning curve on them is steeper than the learning curve of other editors on this list. They're worth mentioning (and its worth learning how to edit files in at least one of them) because one of them is available on virtually every Linux and Unix computer on earth.

Check the documentation for your terminal to see which are installed on your device.

## PyCharm

PyCharm is the most "heavy weight" of all the editors on this list. In fact, it would be more accurate to call it an **Integrated Development Environment** or IDE instead of just an editor. It includes lots of tools for debugging, testing your code, and monitoring plugins. It's available as a paid product from Jetbrains, but students are able to get access for free through their student developer program.

If you haven't programmed before, I would caution you against using this editor; there will be many features and tools that are more complex than you need right now. But by the end of this course, you should be able to make use of some of the more advanced features of PyCharm.

You can apply for the Jetbrains Student Developer tools here. [[LINK](https://www.jetbrains.com/shop/eform/students)].
## Introduction - Python project for beginners

In this article and video, you will learn how to write a simple **Guess-the-number game** in Python using a normal text editor. 

This tutorial is meant to be an easy Python project for beginners, so don't worry if you don't understand everything at first. The main point is to see how **code is just text**. Now let's go build and run your first interactive Python project!

<iframe width="560" height="315" src="https://www.youtube.com/embed/CAOOILNwI5M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Note**: If you don't already have Python installed on your computer, visit <a target="_blank" href="https://www.python.org/downloads/">Python.org</a> to download it. This tutorial is taught for UNIX-based systems (Mac & Linux). If you are on Windows and you don't have Python pre-installed, you can also build the game in an online coding interface, such as [repl.it](https://repl.it/).

## Build the Game 

The first step in building your Python project for beginners game is to write your code in a text editor.

### Coding in your text editor

Open up any Text Editor - this can be as simple as the built-in TextEdit program on MacOS:

![Empty TextEdit Window](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/empty_textedit.png?raw=true)

Code is just plain text. So, if you're using TextEdit, you can press <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>t</kbd> to switch to plain text. Doing so means that you can't apply any formatting, such as bold or italics. Remember that code is just text, so you won't need any formatting for it. Your window should look like this now:

![Plain Text TextEdit Window](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/plain_textedit_window.png?raw=true)

Now it's time to write some code! Type the following code into your TextEdit file:

```python
import random


num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)
    
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")
```
&nbsp;

Make sure you type the code exactly as you see it above, including the 4 spaces for **indentation**. You can also copy-paste the code from [this online resource](https://gist.github.com/martin-martin/d2f0bf7a6187a4e05d847b06e2bcee1d). Your text window should look like this, which is already the full code for this Python project for beginners:

![Code In TextEdit Window](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/guess_code.png?raw=true)

### Save your code!

Finally, let's save your text file using the python file extension `.py`. 

Press <kbd>Cmd</kbd>+<kbd>s</kbd> or go to _File/Save_ and save it on your Desktop with the name `guess.py`:

![Finised Code in TextEdit Window](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/finished_code.png?raw=true)

And that's it for writing the code. Next step is to run the code and play your game.

## Play the Game

Well done so far! :) To play your game on your computer you need to run the Python file you just created. 

### Run your Python project file
To run your Python project on MacOS, open up your **Terminal**. Press <kbd>Cmd</kbd>+<kbd>Space</kbd> to open up Spotlight, and type _Terminal_, then press <kbd>Enter</kbd>:

![How to get to the Terminal](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/get_to_terminal.png?raw=true)

&nbsp;

This will open up your Terminal, a tool that programmers use on a daily basis. If you join one of our courses, you will get to know your Terminal in much more detail, but for this beginner project you don't need to worry about it too much. Just type the following in there:

```bash
cd ~/Desktop
```

![Use cd command to move to your Desktop](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/cd_desktop.png?raw=true)

This will teleport you to your Desktop, where you saved the `guess.py` file that contains your code-text.

![Terminal showing the Desktop](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/on_desktop.png?raw=true)

Now you finally get to play your guess-the-number game. Since you wrote it in Python, you need to also _start_ it using Python. In your terminal, type the following and press <kbd>Enter</kbd>:

```bash
python guess.py
```
&nbsp;

And lo and behold! Here you are! You've officially built and run your very own Python project for beginners game! Now you are ready to play.

![Played Guess-the-number Game in Terminal](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/played_game.png?raw=true)

If you want to play again after it finished, you can press the <kbd>up</kbd> arrow once and your terminal will show you the previous command:

```bash
python guess.py
```

&nbsp;

Pressing <kbd>Enter</kbd> will start the program again from the beginning.

Have fun guessing the number! :D

## Parts of this Python project for beginners

There are a lot of different concepts that went into creating even this very simple Python project for beginners. Let's take a look what they are:

![Base Parts of your Program](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/base_parts.png?raw=true)

In the screenshot above you can see the **filename** of the Python file you created, as well as the **code** saved you saved in the file. Now let's dive deeper into the code and learn about which **programming concepts** you touched upon by making this file.

**Fair warning**: There's a lot going on! Much like a paragraph of English, a script can be broken into many parts: an introductory sentence, references to outside text, subjects, nouns, verbs, and sometimes even new vocabulary.

Keep in mind that, like a paragraph of English, if you understand these parts, then it's likely that you can write and understand another similar paragraph. Even if you haven't seen it before. It also takes some training before you will be able to do that, so don't feel overwhelmed if you won't grasp it all right away. For now enjoy this depiction of the cool code you wrote! :)

![Highlighted Programming Concepts with Labels](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs//programming_concepts.png?raw=True)

We know that is a lot of parts with a lot of colors! If you're intrigued to learn more about writing your own Python projects, check out <a target=_"blank" href="https://codingnomads.co/courses/python-bootcamp-online/">CodingNomads' comprehensive and intutitive Python Programming course</a>. With some time and effort, you will soon be able to grasp these concepts and start speaking the coding language too!

## Tutorial take-aways

- **Code is just Text**: Programming is just writing text, and all you need is a simple text editor to get started!
- **Run using Python**: After writing your code text, you run Python programs with `python`
- **Python project components**: Yes, code is just text... but is it also code :) There are many parts of a Python project, but once you get a grasp you open the door to creating any Python project of your own.

Congratulations again on building your first Python project for beginners!

---

Get started working with one of the most popular programming languages in our [Python Online Bootcamp](https://codingnomads.co/courses/python-bootcamp-online/).

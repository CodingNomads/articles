# Python Project for Beginners

In this article and its related video, you will learn how to write a simple **Guess-the-number game** in a normal text editor. Don't worry if you don't yet understand everything that's going on here, this is a fun python project for beginners. The main point is that you get to see how **code is just text**. Let's go ahead and build and run your first interactive Python program on your own computer.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CAOOILNwI5M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Note**: Depending on what Operating System you are using, Python might not be installed yet. This post won't go into how to install Python. If you are on Windows and you don't have Python pre-installed, you can also build the game in an online coding interface, such as [repl.it](https://repl.it/).

## Build the Game

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

Make sure you type it out as-is, including the 4 spaces for **indentation**. You can also copy-paste the code from [this online resource](https://gist.github.com/martin-martin/d2f0bf7a6187a4e05d847b06e2bcee1d). Your text window should look like this, which is already the full code for your beginner python project:

![Code In TextEdit Window](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/guess_code.png?raw=true)

Finally, let's save it and give it a name, then top it off with the python file extension `.py`. Press <kbd>Cmd</kbd>+<kbd>s</kbd> or go to _File/Save_ and save it on your Desktop with the name `guess.py`:

![Finised Code in TextEdit Window](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/finished_code.png?raw=true)

And that's it for writing the code. You're done with building your first Python project. Next step is for your to run the code to play your game.

### Play the Game

Well done so far! :) To play your game on your computer you need to run the Python file you just created. To do this on MacOS, open up your **Terminal**. Press <kbd>Cmd</kbd>+<kbd>Space</kbd> to open up Spotlight, and type _Terminal_, then press <kbd>Enter</kbd>:

![How to get to the Terminal](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/get_to_terminal.png?raw=true)

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

And lo and behold! Here you are! Ready to play your game:

![Played Guess-the-number Game in Terminal](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/played_game.png?raw=true)

If you want to play again after it finished, you can press the <kbd>up</kbd> arrow once and your terminal will show you the previous command:

```bash
python guess.py
```

Pressing <kbd>Enter</kbd> will start the program again from the beginning.

Have fun guessing the number! :D

## Parts of a Program

There are a lot of different concepts that went into creating even such a small program like this game you wrote. Let's take a look what they are:

![Base Parts of your Program](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs/base_parts.png?raw=true)

In the screenshot above you can see the **filename** of the Python file you created, as well as the **code** saved you saved in the file. Now let's dive deeper into the code and learn about which **programming concepts** you touched upon by making this file.

**Fair warning**: There's a lot going on! Much like a paragraph of English, a script can be broken into many parts: an introductory sentence, references to outside text, subjects, nouns, verbs, and sometimes even new vocabulary.

Keep in mind that, like a paragraph of English, if you understand these parts, then it's likely that you can write and understand another similar paragraph. Even if you haven't seen it before. It also takes some training before you will be able to do that, so don't feel overwhelmed if you won't grasp it all right away. If you do, then wow! If you don't, that's perfectly normal. But check out the pretty colors! :)

![Highlighted Programming Concepts with Labels](https://github.com/CodingNomads/articles/blob/main/code-is-text/imgs//programming_concepts.png?raw=True)

That are a lot of colors! But don't worry if it feels like a lot right now. If you join one of our courses, you will learn to understand all of those programming concepts, and many more! Give it time and effort and you will see that you will be able to grasp it and start speaking the coding language.

Here are the important take-aways from this article:

- **Text**: Programming is just writing text
- **Python**: You run Python programs with `python`
- **Fun**: There's fun stuff you can build! :)

Congratulations again on building your first beginner project in Python.

---

Learn more and get yourself started working with one of the most popular programming languages in our [Python Online Bootcamp](https://codingnomads.co/courses/python-bootcamp-online/).
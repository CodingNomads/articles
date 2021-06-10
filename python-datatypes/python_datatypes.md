## A Quick and Simple Guide to Python Data Types

This blog introduces the most common Python data types, as well as tips for staying sane while learning Python :)

Let’s say you’re just starting out on your programming journey into Python, and you feel like you’re making some progress. You’ve watched some online tutorials, put together a few simple programs, and you're hungry for more. 

You open up Google in your browser and you type ‘python data types’ into the search bar. You’re intent on mastering the basics, and you’re trying to get a better understanding of what types are built into Python. 

You come across this result in your search: https://docs.python.org/3/library/stdtypes.html

You think to yourself that the official documents can’t lead you astray. You click the link. 

You see the page load and the long table of contents listed on the left-hand side. You slowly scroll through the main content on the page and see the word ‘Fraction’ a few times. ‘Binary’. ‘Bytearray’. ‘Bitwise Operations’.

## The secret about Python Data Types

While looking over the Python docs you may feel an acute pang of dread and panic that stalls whatever progress you had, thinking to yourself, “oh my goodness, what am I doing?” You might be inclined to pack it up and call it a day right then and there… 

This is more or less what I did back in 2016, when I packed it up for two years to pursue an entirely different career in personal training. But here I am back at learning Python again. And I wrote this blog to let you in on a secret about Python data types:

You DO NOT need to know all of the details elaborated on the Python docs page. Especially when you’re just starting out. This blog provides a quick and simple guide to the Python data types you need to get started.

## Main Built-in Python Data Types

At a high level, it's good to have a basic understanding of Python's main built-in types to keep in the back of your mind:
-	*Numbers*
-	*Sequences*
-	*Mappings*
-	*Sets*
-	*Booleans*
-	*Classes*
-	*Instances*
-	*Exceptions*

## Most Common Python Data Types

Now in order to really start working with Python, the following data types are the most important to know. Each of these fall within one of the above super categories, and are very commonly used in Python projects.
1.	Integer/`int` (numbers)
2.	Float/`float` (numbers)
3.	String/`str` (sequence)
4.	List/`list` (sequence)
5.	Tuple/`tuple` (sequence)
6.	Set/`set` (set)
7.	Dictionary/`dict` (mapping)
8.	Boolean/`bool` (Boolean)

## Python Data Types Cheatsheet:

In this cheatsheet you'll see that each Python data type has a brief explanation as to what it is, whether they're Mutable or Immutable (changeable or not-changeable), and coded examples that show you what they look like.

| Data Type  | Definition                                                                   | Mutability       | Example                                                                                                                                                                                                                                                  |
| ---------- | ---------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integer    | Positive or negative whole numbers                                           | Immutable        | ```some_int = 252```                                                                                                                                                                                                                                          |
| Float      | Decimal numbers                                                              | Immutable        | ```pi = 3.14159```                                                                                                                                                                                                                                             |
| String     | Text wrapped in quotes                                                       | Immutable        | ```single_quote_string = 'A single quote string'```<br>```double_quote_string = "A double quote string"```<br>```multi_line_string = """ For when you have lots of text.```<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```This makes it easier to read.```<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```It's best not to have one really```<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```long line."""``` |
| List       | Square brackets that encase elements separated by commas                     | Mutable          | ```fruit_list = ['apple', banana', 'mango', 'pineapple']```                                                                                                                                                                                                 |
| Tuple      | Values separated by commas; generally encased in parentheses                 | Immutable        | ```some_tup = 1, 'Hello!', 3.14159```<br>```another_tup = ([apple, banana], 'Groceries', 20.00)```<br>```cast_tuple = tuple([apple, banana, mango])```<br>```singleton_tup = (, )```                                                                                      |
| Set        | Unordered collection with no duplicate elements                              | Mutable          |  ```url_list = ['http://www.example.com', 'http://www.setsareuseful.com', 'http://www.example.com']```<br>```unique_urls = set(url_list)```<br>```print(unique_urls)  # OUTPUT: {'http://www.example.com', 'http://www.setsareuseful.com'}```                        |
| Dictionary | Curly braces that encase key and value pairs, which are separated by a colon | Immutable = Keys | ```some_dict = {'Scott': 'scott@email.com'}```<br>```Key = 'Scott'```<br>```Value = 'scott@email.com'```                                                                                                                                                                  |
| Boolean    | Code logic that evaluates to TRUE or FALSE                                   | Depends          | ```if 1 < 2: # This is True, so indented code will get executed```<br>```if 1 > 2: # This is False, so indented code wont get executed```                                                                                                                              |

## Takeaway
During your day-to-day work with Python, these are the meat and potatoes of the data types that you'll be working with. But another important takeaway is that when going over documentation, you're not expected to know every little detail. 

As you continue to work through projects, you'll gain a better understanding of what exactly it is that you'll need to know. In the meantime, here are some more tips to help you learn to code more effectively:
1. Use Google. It'll be your best friend, not only as a beginner, but likely for as long as you're programming
2. When confronted with documentaion that's intimidating, enter `control + F` and search for whatever term it is that you're trying to read up on
3. Join online forums or study groups. The learning process is a lot more enjoyable when you're a part of a friendly and knowledgable community. This is why I decided to learn Python with CodingNomads, and why I'm able to share with you these tips today! ;)

## A Quick and Simple Guide to Python Data Types

This blog introduces the most common Python data types, as well as tips for staying sane while learning concepts like these as a beginner.

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

## Python Data Types Overview/Cheatsheet:

Below, each Python data type has a brief explanation as to what it is, followed by examples showing what they look like, and whether they're Mutable or Immutable (changeable or not-changeable).

### 1. Integer

- ```int```: Positive and/or Negative whole numbers
- ```some_int = 252```
- **IMMUTABLE DATATYPE**

### 2. Float

- ```float: Decimal numbers ```
- ```pi = 3.1415```
- **IMMUTABLE DATATYPE**

### 3. String

- ```str```: text wrapped in quotes
- ```single_quote_string = 'I am a string in single quotes'```
- ```double_quote_string = "This is a string in double quotes"```
- ```multi_line_string = '''Triple quotes... For when you have lots of text. It's easier to read this way'''```
- **Special Note**: 
    - You cannot mix quote types.
    - They must start and end with the same type
- **IMMUTABLE DATATYPE**


### 4. List

- ```list```: elements separated by comas, encased by square brackets
- ```some_list = ['banana', 'apple', 'mango']```
- **Mutable Datatype**

### 5. Tuple

- ```tuple```: values that are separated by commas, wrapped in parentheses
- ```some_tup = 1, 2, 'Hello'```
- ```another_tup = (1, 2, 'Hi!')```
- ```wrap_tup = tuple(1, 2, 'Konnichiwa!')```
- ```singleton_tup = (, )```
- **IMMUTABLE DATATYPE**

### 6. Set

- ```set```: an unordered collection with no duplicate elements
- ```some_set = {1, 2, 3}```
- ```another_set = set([1, 2, 3])```
    - *Practical Example*:
    - ```url_list = ['http://www.example.com', 'http://www.setsareuseful.com', 'http://www.example.com']```
    - ```unique_urls = set(url_list)```
    - ```print(unique_urls)  # OUTPUT: {'http://www.example.com', 'http://www.setsareuseful.com'}```
- **Mutable Datatype**

### 7. Dictionary

- ```dict```: key and value pairs separated by a colon, which are encased in curly braces
- ```some_dict = {'Scott': 'scott@email.com'}```
    - ```key = 'Scott'```
    - ```value = 'scott@email.com'```
    - ```print(some_dict['Scott']) #OUTPUT scott@email.com```
- **KEYS = NEED TO BE IMMUTABLE DATATYPE**

### 8. Boolean

- ```bool```: 
    - fundamental building block of computers; representation of binary
    - useful when testing for 'truthness' with comparison operators
    - `True` / `ON` / `1`
    - `False` / `OFF` / `0`
    - *Practical Example*
        - ```if 1 < 2:  #THIS IS TRUE, SO INDENTED CODE BELOW WILL GET EXECUTED```
        - ```if 1 > 2:  #THIS IS FALSE, SO INDENTED CODE BELOW WILL NOT GET EXECUTED```

## Takeaway
During your day-to-day work with Python, these are the meat and potatoes of the data types that you'll be working with. But another important takeaway is that when going over documentation, you're not expected to know every little detail. 

As you continue to work through projects, you'll gain a better understanding of what exactly it is that you'll need to know. In the meantime, here are some more tips to help you learn to code more effectively:
1. Use Google. It'll be your best friend, not only as a beginner, but likely for as long as you're programming
2. When confronted with documentaion that's intimidating, enter `control + F` and search for whatever term it is that you're trying to read up on
3. Join online forums or study groups. The learning process is a lot more enjoyable when you're a part of a friendly and knowledgable community. This is why I decided to learn Python with CodingNomads, and why I'm able to share with you these tips today! ;)

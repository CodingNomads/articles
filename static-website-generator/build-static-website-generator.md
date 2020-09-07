In this video and transcript you will learn about how to automate the process of building HTML sites from your plain text notes to create a travel blog.

Watch the video below for the walk-through, and read the transcript attached below for quick reference:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ek2QEQZq9KY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Transcript

Today I want to show you how to automate a tedious process with Python.

Say you're writing a travel blog and you have all these `.txt` files of places that you visited, and you want to transform them into **HTML pages** so that you can display them on your website.

But typing all of this into HTML, sounds really annoying. Because of that we're going to write a Python script to do exactly that. The script will be fetching all the `.txt` files that are inside of the `raw/` folder and convert the content to HTML, and then create new files in here in the `pages/` folder, that are going to be fully finished HTML pages that you can pop into your website.

We're going to at first have to fetch a list of all the raw text files in that folder. We're going to need a module, `os`, from the standard library:

```python
import os
```

And then we're going to go to fetch the `raw_files`, everything inside of `raw/`:

```python
raw_files = os.listdir('raw')
```

It's going to be a list that is starting here, a list of file names. Okay. Let's iterate over those:

```python
for file in raw_files:
```  

First, we're going to have to read in the file contents:

```python
    with open('raw/'):
```

Here, we're fetching the file from the `raw/` folder. And then here, we're going to pop in the file name that we're getting from iterating over it:

```python
    with open(f'raw/{file}'):
```

And we're opening this in **read** mode and let's declare a encoding, just to be on the safe side, UTF-8, as `f`:

```python
    with open(f'raw/{file}', 'r', encoding='utf-8') as f:
```

And let's get the title first. How would that look like? We know that, we know that the first line of our text is going to be the **title**. So let's get this one out of there by using `f.readline()`:

```python
        title = f.readline()
```

That just reads one line until it reaches a _newline character_ `\n`, and we're going to right away strip off the newline character because we don't need it in the title:

```python
        title = f.readline().rstrip()
```

And next we're going to go get the content. Let's start off with an empty string:

```python
        content = ""
```

That we're going to fill up by going over each remaining line:

```python
        for line in f.readlines():
```

Like this, we go over all the lines, but we don't want the title line again. So I'm just going to start after the first one:

```python
        for line in f.readlines()[1:]:
```

So with the second one, that's the index number one in programming. And from there, we're going to go to the end.

And now we're going to add to the content and what are we going to add? We're going to add a string that consists of `<p>`s, so these are paragraphs in HTML:

```python
        for line in f.readlines()[1:]:
            content += f"<p></p>"
```

And inside of each of these `<p>`s, we're going to want to have, let's build this back together as a string. We're gonna get the line without the newline character. And here we go, we're building it back together because this exists as a list. And we want, we want to have it as a string:

```python
        for line in f.readlines()[1:]:
            content += f"<p>{''.join(line.rstrip())}</p>"
```

So we're popping the string of the line inside of a `<p>` tag that we're going to add to our `content`. And we do this for every line in there.

And then, and then we're going to build the page! `page` is going to be, let's make this three strings:

```python
        page = f"""<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>

</body>
</html>
"""
```

And here I have code base that's just the basic HTML structure. We're going to need the `DOCTYPE` declaration, `<head>` with a `<title>`. And right in here, we can put our title:

```python
        page = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>

</body>
</html>
"""
```

We're going to want to use it again in the body as a heading, like so. And then we're going to put all our--Ah so I forgot to put it in, here's the title:

```python
        page = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
</body>
</html>
"""
```

And then they're going to put all our `content` that we just got before:

```python
        page = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    {content}
</body>
</html>
"""
```

And that's basically our HTML page. It's going to get filled up with the `title`, which is the first line of our `.txt` file that comes in as the `<title>` of the page, and then also as a title _on_ the page. And then we're going to fill it up with `content` consisting of `<p>` tags for every paragraph that's inside of our text file.

That was filling up to basic HTML structure. Let's put it here. I have to comment this on place. Okay.

And then finally--Watch out! We have to be _in the indentation_! We're out here only because we want to make the HTML page look nice and having three double quotes takes the formatting _exactly_ how it is in this string.

And finally, we write this content into a new HTML file. Let's just call it the same that we call the other one before, but we want it inside of the `pages/` folder and then our file name:

```python
        with open(f'pages/{file}'):
```

However, we don't want this to be a `.txt` file, but we want it to be a `.html` file:

```python
        with open(f'pages/{file}.html'):
```

So we're going to have to remove the extension in here. Let's take off the last four. That's going to be `txt` and the `.`:

```python
        with open(f'pages/{file[:-4]}.html'):
```

And then we're going to add it here with `.html`. And we're opening this as the **write** mode:

```python
        with open(f'pages/{file[:-4]}.html', 'w') as f:
```

And then finally write the contents of the page that we have in here to our file object:

```python
        with open(f'pages/{file[:-4]}.html', 'w') as f:
            f.write(page)
```

And that's it. Now take a close look up here on the `pages/` before I run this. You're going to see two pages popping up that are going to be our process text files turned into HTML pages. There we go. One, two, three.

There they are, let's take a look. It's nicely formatted HTML. We have a `<title>`, we have a heading, then we have multiple `<p>` tags in there. And let's take a look how this looks like in a browser.

There you go. It's a proper HTML page. It's not nicely formatted, but you might already have your CSS. So you just read the CSS. 

But that's an easy way to get text files and transform them into HTML pages that you can serve right away, for example, on GitHub.

---

Here is the full code again, so you're able to look at it all in one place:

```python
import os


raw_files = os.listdir('raw')

for file in raw_files:
    with open(f'raw/{file}', 'r', encoding='utf-8') as f:
        title = f.readline().rstrip()
        content = ""
        for line in f.readlines()[1:]:
            content += f"<p>{''.join(line.rstrip())}</p>"
        page = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    {content}
</body>
</html>
"""
        with open(f'pages/{file[:-4]}.html', 'w') as f:
            f.write(page)
```

Hopefully this quick tutorial on writing an automatic website generator in Python was helpful for you and can get you started making it easier to build your travel blog.

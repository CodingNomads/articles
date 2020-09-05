This series of blog posts will help you get started with the Django Web Framework. Learn more and dive deeper in our intensive [Django Online Bootcamp](https://codingnomads.co/courses/django-course-learn-django-online).

Let's learn about **Django Files**. When you create a new Django application with the `startapp` command, you end up with a whole lot of files. This might seem overwhelming when you see it the first few times.

In this video, you will learn about what are the most important files, and what they are used for in a Django app, and which files can you ignore for the start. You can read the transcript of the video below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/5nkmA6OY148" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Transcript

In this video, we're going to take a look at the most important Django files and folders. And remember, we're still just browsing. So just look and enjoy.

The most important ones, the files we're going to work with are:

- `settings.py`
- `urls.py`
- `views.py`
- `models.py`
- and the folder `templates/` where we're going to have our templates inside.

Don't worry if you don't know what that means right now. I'm just going to give you a quick overview in the code.

So this is the same structure that we looked at before. We have the management app called `myproject`. Same as the project that we called it. And in here, the two files that we're going to touch is `urls.py`  and `settings.py`.

The settings file contains a ton of code that just comes pre-generated and this might be-- so the whole thing why I'm doing this overview is that all of these files and folders, they might seem a little intimidating at the beginning.

And then you look at this file and there's all this code in there, right? Don't worry about it too much. Okay? So there's really not that much that we're ever going to have to change inside of the set`settings.py` file at the beginning when getting to know Django, but every once in a while, we're going to come over here and then add a little line maybe here, et cetera.

Don't get too intimidated as the main point of what I'm trying to say here. `settings.py` is not too bad and it's like a control center of your project. So that's an important one.

Then we have `urls.py`. There's also a bunch of code in here, but this helps us to route things around. And I'm going to talk more about this in the next video. For now just remember, like `settings.py` and `urls.py` in the management app are the two important files.

And then in any app that we're going to create, so our `blog` app that has a bunch of different files. The most important ones are going to be `models.py` where we're defining how should the data look like that goes into our database.

`views.py`, where we're putting our code logic, actually where we're writing the code, that does something with the data that's inside of the database, and then passes it forward to a folder that we're going to have to create.

And I'm just going to show you that right now, we want the folder in here called `templates/`. And in here, we're going to have HTML templates that are going to get rendered.

And another file that we need in here that doesn't come right away is `urls.py`. So we have in each app, we're also going to have -- I'm gonna make it a bit smaller -- In each app. We also going to have a `urls.py` file. And that is because we're going to route from our management app -- we're going to use this one -- to point us forward to this file. And then this `urls.py` file helps `views.py` know what to pick from models and where to put it in `templates/`.

But I've kind of talk about the Flow of the Django app that I just mentioned here quickly in more detail in the next video.

As a sum up: the important files in here:

**Management App**:

- `settings.py`
- `urls.py`


And in our app that we're working with, where we're spending most of our time, it's going to be:

- `views.py`
- `urls.py`
- `models.py`
- and then the `templates/` folder

So, here we are: `settings.py`, `urls.py`, `views.py`, `models.py`, and `templates/`. That's what we're going to focus on.

Don't get intimidated. It's really not too bad. And in the next video, we're going to talk about the Flow. And I'm going to explain to you how stuff moves through a Django app. And that's going to be helpful for later on when we're going to build it out. Okey Dokey, see you there.

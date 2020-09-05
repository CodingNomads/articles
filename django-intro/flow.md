This series of blog posts will help you get started with the Django Web Framework. Learn more and dive deeper in our intensive [Django Online Bootcamp](https://codingnomads.co/courses/django-course-learn-django-online).

Let's learn about the **Django Flow**. What happens inside your Django app when you go to your browser and want to see a page of your project?

In this video, you will learn about how a **request** flows through your Django app, which files it hits as well as in which order, and why each of them is part of the flow. This will give you a helpful high-level overview of the internal functionality of a Django app. You can read the transcript of the video below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/JndxWxExPFM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Transcript

What happens in Django when you go to a URL and it loads the page, or you click a button and it moves somewhere. What's going on behind the scenes? So this is what I call the **Django Flow**. And in this video, we're going to take a quick look at what are the different pieces that work together to make this possible, so that we're able to move from a URL like this one over to a page that actually displays some data.

There's something going on in between: that's the Django "black box" (or a "green box" in that case). What's happening in here? And we're going to unravel that right now.

I'm calling this the _Django Flow_ because it's kind of like a river moving down. And maybe at the beginning, this might look more like a intimidating wave. And maybe you're like this little otter and you feel swept away by it. So don't worry too much, we're going to talk about this a bit. And then eventually the aim is that you're going to be surfing this wave and understand how the flow of Django works. Just have fun with it!

Okay. So first of all, we're in the browser and we're going to this URL here. In that case that's on our `localhost` and it has a certain end point here that we're hitting. So we're here and pressing <kbd>Enter</kbd>, that's step number one.

So now we're moving into Django, and I've represented this here with our folder structure. The one we looked at already before in Visual Studio Code, and I'm going to step you through different files that are going to get addressed .

**`project/urls.py`**: So, after hitting the URL, the first point inside of our app is your `ulrs.py` of the _project_. This is the _management app_ that comes with the same name as the Django project that we're creating. And in here, we have a `urls.py` file and that's the first place that gets addressed.

**`app/urls.py`**: From there it directs us forward to the `urls.py` file inside of the _app_. So now we're inside of a Django app. Remember, we can have more of those, but in this case, we just have one. `urls.py` points us forward to `views.py`.

**`views.py`**: That's where the code logic sits. And this generally draws some stuff from the _models_, some information through `models.py` from the database and then points us forward to templates.

**`templates/`**: And then inside of templates is the HTML file that gets rendered. And eventually this is what is going to get displayed.

And as parts of this HTML file that gets built with the information we drawing from the models inside of `views.py`, those are the steps that we go through. Okay. And we end up with this beautiful website here.

Still feels a bit like too much, and like the wave's crashing over you? So we're going to go through the whole process again with a slightly different one. This is going to get familiar.

Now we're looking at a different page. We're looking at the individual page of a blog. We looked at this before as well. And the flow is going to be very much the same. So we click on the URL. Next thing it goes into `urls.py` off the management app, points us forward to `urls.py` inside of the app.

Next thing we go to `views.py` where the code logic lives. This draws some stuff from `models.py` and points forward to the `templates/`, the templates generate the HTML page. And finally it gets rendered again, back in the browser.

All right. Feels a bit more like surfing already! Don't worry if you don't get it yet all the way, during this course, I'm going to try to get you to a point that you feel like you're surfing this Django Flow wave. And just by doing it many, many times and understanding what is inside of all these different files, you're going to get a good feeling for what's going on. And the Django Flow is going to start to feel familiar.

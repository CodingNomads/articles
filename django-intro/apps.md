This series of blog posts will help you get started with the Django Web Framework. Learn more and dive deeper in our intensive [Django Online Bootcamp](https://codingnomads.co/courses/django-course-learn-django-online).

Let's learn about **Django Apps**. Django makes a distinction between a _project_ and an _app_, where you can think of the project as a higher-level structure that can include multiple apps. Django apps are pluggable, which means that you can re-use them in a different project. This makes Django apps very versatile.

Watch the video below for a high-level overview of what Django apps are all about. You can read the transcript of the video below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/bxQQ-HnIKmk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Transcript

Let's take a look at Django apps. And just as a little heads up at the beginning, this is a joy ride. So I don't want you to code along. I don't want you to even necessarily try to remember everything that's going on. This is going to be a very high-level overview, just to get you familiar with what's going on. And we're going to walk through all of these things that I'm touching on now, later in a way that's going to be just step by step and then trying to understand what's actually happening.

For now, just joy ride, so I want you to just relax and enjoy the view from up there. Okay. And to remember that I popped up this little symbol up here in the top, right? So just for you to remember that whatever slide comes up in the section, just let it flow over you. And I'm going to promise you that you'll understand later on better what's going on.

Okay. So let's get going with **Django Apps**. The first thing to remember with Django apps is that a Django _project_ is not a Django _app_. Those are two different things. And in fact, the project is a higher-level structure that contain a multitude of apps. There can be a couple of apps in each Django project. So you can think of it like this, that project is the top level thing, and then you can have one app, two apps, or as many apps as you want inside of a Django project.

Let's take a look at how that's like inside of code. So I'm over here in Visual Studio and I'm showing you here just a standard Django project that I created before that I called `myproject`. Whatever the name is going to be would pop up here.

And by creating this project, it also creates another folder inside called `myproject` as well. And a couple of files. And `manage.py` who we're going to look at that later.

But this, `myproject` gets created together. And this is the so-called **management app**. This app gets created when you make the project -- remember _project_ -- and the contents are somewhat different to the contents of an Django _app_.

You have here the `wsgi.py` file for example, and the `settings.py` file. There's a lot of code in there and you'll learn more about all of this. You don't really need to know about it now, but just keep in mind that there's this management app that is kind of like on the _project level_ structure. So, this lives up here, the management app. Okay.

And then we have apps inside, and that is app 1 or 2 that I showed before. And those get created in a different way. And we can have a ton of those in there and they have somewhat different files living inside of them. You see this folder here and `admin.py`, `apps.py` -- it looks a bit different.

But any new app that I'm going to create is going to look _exactly_ like this one. So if I hop over here and I say `manage.py` -- and I'm just going to make a second one, and I call it `myapp2` -- see another folder pop up here. And the content in here is the same as the content in here.

So any new app that you're going to create is going to be the same. And that's just a structure that helps you to get started building the app. And it also highlights the **pluggable nature** of Django apps.

So what's cool about this is that we can take this folder, essentially it's just a folder with a bunch of files in there, and you could reuse it in a different Django project.

So if you build out a blog, for example, and you want to use a blog in your portfolio app, maybe you're going to build a portfolio for yourself. And you also want to have a blog there. You could create the whole blog app in here. Everything is contained that you need. And then you just pick up the folder -- it's literally just a folder -- pop it over in your other project and you can reuse the code over there. That's one of the cool things about Django: the _pluggable nature_ of its apps. I hope that makes sense.

So quick recap, we have a **management app** that gets created together with the project, a little bit different, the most important file is `settings.py`. And then we have **apps** in there that contain features of different sections of your project, so to say. We create them with `python manage.py startapp <app_name>` and they all kind of look the same, until we change them. That's all for the apps. Let's take a look at files next. 

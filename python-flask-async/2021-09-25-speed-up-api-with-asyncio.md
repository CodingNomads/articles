---
title: Speeding Up API Endpoints using Python AsyncIO
date: 2021-09-25T12:19:01-07:00
categories:
    - code
    - python
draft: true
---

- [One App, Two Endpoints](#one-app-two-endpoints)
- [Two Endpoints, One Fast, One Slow](#two-endpoints-one-fast-one-slow)
- [Timing the Results](#timing-the-results)
- [A Real World Use Case](#a-real-world-use-case)
- [Conclusion](#conclusion)

As a developer, you want the APIs you write to be as fast as possible. So what if I told you that with one trick,
you might be able to increase the speed of your API by 2x, 3x, or maybe even 4x? In this article you will
learn how to utilize Python **asyncio**, the **HTTPX** library, and the **Flask** micro framework to optimize certain parts of your API.

**In this tutorial you will:**

1. Write a small HTTP API using everyone's favorite Python framework: <a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank">Flask</a>.
2. Use <a href="https://www.python-httpx.org/" target="_blank">HTTPX</a>, an awesome modern Python HTTP client that supports async.
3. Familiarize yourself with a small subset of Python's <a href="https://docs.python.org/3/library/asyncio.html" target="_blank">asyncio</a> library.

Hold on tight, you're about to speed up your Flask API endpoints using Python's `asyncio`!

<h2 id="one-app-two-endpoints">One App, Two Endpoints</h2>

To begin this feat of strength, you will write a simple Flask app with two endpoints. One will be asynchronous and the other will not.

>**Note:** For maximum compatibility, please make sure you are using Python **3.8** or newer.

Begin by creating a directory to hold your code and create a virtual environment in it:

```bash
mkdir asyncapi
cd asyncapi
python3 -m venv env/
```

Activate the virtual environment and install Flask with async support:

```bash
source env/bin/activate
python -m pip install "Flask[async]"
```

Next, place the following code in a file named `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/get_data')
def get_data():
    return 'ok'

@app.route('/async_get_data')
async def async_get_data():
    return 'ok'
```

You now have a fully working Flask API with two endpoints. If you are new to Flask and are curious what is going on here, check out the <a href="https://flask.palletsprojects.com/en/2.0.x/quickstart/" target="_blank">Flask quickstart documentation</a>
or dive deep into <a href="https://codingnomads.co/courses/flask-tutorial-python-flask-apps-online-course" target="_blank">web development with Flask</a>.

Notice that the second endpoint, `/async_get_data` uses the `async def` syntax for defining it's method. Still, this endpoint does exactly the same as the normal `/get_data` endpoint, except that you can run asynchronous code in it. As it is written now, however, it is not any faster. You can prove this by running our API and making a few calls with **cURL**.

Start the Flask development server:

```bash
flask run
```

With your development server up and running, you can use `time` in a new terminal to show
that the execution time of cURL requests to both endpoints return in about the same time.

>**Note**: The following command output may look different depending on which operating system and shell you are using. As long as you have the `time` command, you should be able to see the result.

First, measure the synchronous endpoint:

```bash
time curl "http://localhost:5000/get_data"
ok
________________________________________________________
Executed in    7.28 millis    fish           external
   usr time    5.86 millis  248.00 micros    5.61 millis
   sys time    0.03 millis   32.00 micros    0.00 millis
```

Notice the line that says "Executed in 7.28 millis". That's pretty quick.

Now use `time` again to measure the the async endpoint:

```bash
time curl "http://localhost:5000/async_get_data"
ok
________________________________________________________
Executed in   21.77 millis    fish           external
   usr time    2.48 millis    0.00 micros    2.48 millis
   sys time    2.77 millis  293.00 micros    2.48 millis
```

Are you surprised to see that the asynchronous version was slower?

The asynchronous request took about 3x longer than the synchronous request!
The difference between 7 miliseconds and 21 miliseconds is not noticeable to the human eyes.
Still, this is a good demonstration that there can be overhead to using `asyncio`,
so it is not faster in *all* situations.

<h2 id="two-endpoints-one-fast-one-slow">Two Endpoints, One Fast, One Slow</h2>

In order to see the `async_get_data` endpoint become faster than it's sync counterpart, you'll have to make the endpoints actually do some work. One common case for APIs is that they need to make calls to other APIs, for example, to fetch the weather for a specific location from a third party service.

You can add HTTP requests to your API using a combination of `httpx` and <a href="https://flash.siwalik.in/" target="_blank">Flash</a>, a service that intentionally returns slow HTTP responses. Why slow? Because you want to be able to simulate large and or slow external APIs which will help exaggerate the effect of using `asyncio`.

First, install the `httpx` library:

```bash
python -m pip install httpx
```

Modify `app.py` to look like this:

```python
from flask import Flask
import asyncio
import httpx

app = Flask(__name__)


@app.route('/get_data')
def get_data():
    response_1 = httpx.get('https://flash.siwalik.in/delay/1000/')
    response_2 = httpx.get('https://flash.siwalik.in/delay/1000/')

    return {
        'response_1': response_1.status_code,
        'response_2': response_2.status_code
    }


@app.route('/async_get_data')
async def async_get_data():
    async with httpx.AsyncClient() as client:
        coroutine_1 = client.get('https://flash.siwalik.in/delay/1000/')
        coroutine_2 = client.get('https://flash.siwalik.in/delay/1000/')
        results = await asyncio.gather(coroutine_1, coroutine_2)

        return {
            'response_1': results[0].status_code,
            'response_2': results[1].status_code
        }
```

Both endpoints now make two GET requests to https://flash.siwalik.in/delay/1000/, which returns a simple response after one second. The first function `get_data()` should look familiar to anyone who has used the Python `requests` library. `response_1` contains the result of the first API call, and `response_2` contains the result of the second API call. The method then returns the status code of each response.

The second function, `async_get_data()`, looks a bit different, although the end result is the same. Going step by step, this is what is happening:

```python
async with httpx.AsyncClient() as client:
```

The code creates an asynchronous context manager which makes the `client` object available. This is the same thing as a normal context manager, except that it allows the execution of asynchronous code. `client` is what makes the actual HTTP calls.

Next, you assign two variables to the results of calling `client.get()` on the two API calls to the Flash API:

```python
coroutine_1 = client.get('https://flash.siwalik.in/delay/1000/')
coroutine_2 = client.get('https://flash.siwalik.in/delay/1000/')
```

At first you might assume that the results of the API calls will be stored in these variables but actually `coroutine_1` and `coroutine_2` are co-routines, not HTTP responses.

```python
results = await asyncio.gather(coroutine_1, coroutine_2)
```

Now the magic of async happens. Here the return value of `asyncio.gather()` is assigned to the `result` variable, and it is awaited. When you see the `await` keyword, it means that the code will block execution there until the call to a co-routine is complete. The `.gather()` method itself is a co-routine, and will execute a sequence of other co-routines (like `[coroutine_1, coroutine_2]`) *concurrently*, and then return a list of results.

Finally, the method returns the status code for each HTTP response by accessing it within the array of results.

```python
return {
    'response_1': results[0].status_code,
    'response_2': results[1].status_code
}
```

Calling `get_data()` and `async_get_data()` should result in the exact same result, but `async_get_data()` will complete much faster. How much faster do you think it will finish?

<h2 id="timing-the-results">Timing the Results</h2>

Now that you have an API with two endpoints that do the same thing, except one is asynchronous and one is not, you should return to using cURL to time them.

>**Note:** At this point, you may have to restart the Flask dev server to pick up your changes.

Start with `get_data`:

```bash
time curl "http://localhost:5000/get_data"
{"response_1":200,"response_2":200}

________________________________________________________
Executed in    3.56 secs      fish           external
   usr time    0.29 millis  295.00 micros    0.00 millis
   sys time    5.00 millis   48.00 micros    4.96 millis
```

You can see that both responses return an <a href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_success" target="_blank">HTTP 200</a>, and in total your endpoint took about 3.5 seconds to return. That makes sense: the external endpoints provided by Flash paused for one second each and the extra 1.5 seconds of other overhead can be accounted for in DNS lookups, TCP connections, slow Comcast internet, and other internet related spaghetti.

Next, try timing the `async_get_data` endpoint:

```bash
time curl "http://localhost:5000/async_get_data"
{"response_1":200,"response_2":200}

________________________________________________________
Executed in    1.81 secs      fish           external
   usr time    6.21 millis  342.00 micros    5.87 millis
   sys time    0.06 millis   59.00 micros    0.00 millis
```

If in the previous section you guessed that the async version would be about twice as fast, you are correct! Why? Because Flask ran the calls to the external API concurrently. That means that in this case, the entire act of retrieving the results from the Flash API was only as slow as the slowest call.

In fact, you can try adding a third call to each method. The first endpoint will take roughly 1.5 seconds longer, while the async version will still execute in roughly 1.8 seconds. You can keep adding HTTP calls to the async version and it should *continue* to return in roughly the same amount of time until you start hitting various hardware, network and operating system level constraints.

<h2 id="a-real-world-use-case">A Real World Use Case</h2>

HTTP calls aren't the only place where asyncio can make a difference. In fact, you can see other use cases right there in the name of the Python module: `asyncio` stands for Asynchronous Input/Output.

Many APIs are backed by databases and getting the results of a SQL query from a database server is often bound by I/O. You could replace one of the calls to the Flash API in our app with a call to a database instead. Imagine this DB call takes 500 milliseconds to return.

The **synchronous endpoint**, `get_data`, takes roughly **1.5 seconds** to return the result:

 - 1 second for the HTTP call
 - 0.5 seconds for the database call

 The **asynchronous endpoint**, `async_get_data`, takes roughly **1 second** to return the result:

- 1 second for the HTTP call
- 0.5 seconds for the database call

Even though the individual calls take the same amount of time, they both execute *concurrently*.
This means the total time is only as long as it takes the slowest operation to return the result.
You just saved 0.5 seconds by using `asyncio`!

Keep in mind that if you need the results of one async call for the next async call, this won't be much help.
In that case you can only start running the second call when the first one is complete,
which would bump your total time back to a synchronous execution time.

<h2 id="conclusion">Conclusion</h2>

In this article you learned how Python's `asyncio` can speed up your application considerably in situations where your code is waiting on multiple instances of Input/Output. You also learned how `asyncio` can be used effectively and easily with the Flask web framework and the HTTPX library.

`asyncio` won't always make your API faster, but in certain situations it can make a huge difference like demonstrated in this tutorial. Keep what you learned here in mind when writing your code in the future and you might gain some easy performance wins!

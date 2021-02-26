- [Gotta go Fast: Writing an API with Python and FastAPI](#gotta-go-fast-writing-an-api-with-python-and-fastapi)
  - [Setting up the Project](#setting-up-the-project)
  - [Starting with "Hello World"](#starting-with-hello-world)
  - [Defining Models and Business Logic](#defining-models-and-business-logic)
  - [Adding a Database](#adding-a-database)
  - [Conclusion](#conclusion)

# Gotta go Fast: Writing an API with Python and FastAPI

One of the many great reasons to use Python for development is the vast amount of mature and stable libraries to choose from. When it comes to web development, <a href="https://codingnomads.co/courses/django-course-learn-django-online" target="_blank">Django</a> and <a href="https://flask.pocoo.org" target="_blank">Flask</a> offer a great development experience and troves of documentation that has been written over the years.

Recently the Python ecosystem has been seeing some exciting new development powered by new features available only in Python 3+ such as <a href="https://docs.python.org/3/library/asyncio-task.html" target="_blank">coroutines</a> and <a href='https://docs.python.org/3/library/typing.html' target='_blank'>optional typing</a>. This new era of libraries and frameworks promise both greater speed and ease of development to bring Python on par with newer languages like Go and Rust, while keeping the core experience that has made Python so popular.

<a href="https://fastapi.tiangolo.com" target="_blank">FastAPI</a> is one of these new frameworks for developing web APIs that has been gaining popularity over the last few years. If you are planning on doing web development with Python now or in the future, it would be a good idea to be familiar with it.

In this tutorial, you'll build an API for a database of remote working locations
using FastAPI. Coding Nomads are always in need of good coffee and wifi while on
the road. With this API, you can ask your friends from all over the world to
submit their favorite places so that you'll always know the best place to go no
matter where you are.

In this article you will:

- Create a new FastAPI project from scratch.
- Create an API for fellow coding nomads to submit remote working locations.
- Save the app's data to a real database using an ORM.

Get ready to build your tool to locate the best remote working locations for your fellow
travelers, and learn to use the modern Python FastAPI library on the way.

<h2 id="setting-up-the-project">Setting up the Project</h2>

To get started you will go through the usual Python project setup steps. By the end of this setup, you'll have a base project that can be re-used for other FastAPI projects.

First, create a new folder for your project. Then create a new virtual environment inside it:

```bash
mkdir fastnomads
cd fastnomads
python3 -m venv env/
```

This will ensure the Python packages we install stay isolated to the project.

Next, activate the virtualenv:

```bash
source env/bin/activate
```

Now you can install FastAPI and uvicorn, an ASGI server:

```bash
pip install fastapi uvicorn
```

And now you should be ready to write some code.

<h2 id="starting-with-hello-world">Starting with "Hello World"</h2>

Before you delve into coffee shops and libraries, you should have the traditional "Hello World" app up in running in FastAPI. This will allow you to prove that your initial setup is working properly.

Open up your favorite editor and paste the following code into a file called `main.py`. You'll use this file for the remainder of your development:

```python
from fastapi import FastAPI, Depends

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World!'}
```

In just these five lines of code, you've already created a working API. If you've ever used Flask this should look very familiar. The last three lines are the most interesting.

This is a route:

```python
@app.get('/')
```

It tells FastAPI that the following method should be run when the user requests the `/` path.

This is a method declaration:

```python
async def root():
```

Notice the `async def`: this method will be run as a Python3 coroutine! If you'd like to learn more about concurrency and async, FastAPI itself has a <a href='https://fastapi.tiangolo.com/async/)' target='_blank'>great explanation</a> of the whole thing and what makes it so fast.

Finally, the return statement where we send the data to the browser:

```python
    return {'message': 'Hello World!'}
```

As you might expect, visiting this endpoint will return a JSON response matching the dictionary above.

Enough talk, run the server to see it in action!

```bash
uvicorn main:app --reload
```

Now try visiting <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a> in your browser. You should see this:

```json
{ "message": "Hello World!" }
```

Perfect. But that's not it, FastAPI has also automatically generated fully interactive API documentation that you can use to interact with your new API. Visit <a href="http://127.0.0.1:8000/docs" target="_blank">http://127.0.0.1:8000/docs</a> in your browser. You should see something like this:

![Landing page of the auto-generated API docs](https://github.com/CodingNomads/articles/blob/main/fastapi-tutorial/apidocs.png?raw=true)

In this image you can see the endpoint that was just defined, and even execute it straight from your browser!

Since you are creating an API only with no frontend user interface, you'll be using the interactive documentation as the main method of interacting with the API.

<h2 id="defining-models-and-business-logic">Defining Models and Business Logic</h2>

Now it's time to take your application beyond the basics and start writing code specific to your goal.

The first thing you are going to do is create a <a href="https://pydantic-docs.helpmanual.io" target="_blank">Pydantic</a> model to represent a `Place`. Pydantic is a data validation library that uses some neat tricks from the Python3 type system. FastAPI relies heavily on it to both validate incoming data and serialize outgoing data.

You'll also define a route to create a new `Place`. For now all it will do is return the submitted `Place` back to you.

Add the following code so that your `main.py` looks like this:

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float

    class Config:
        orm_mode = True

@app.post('/places/')
async def create_place_view(place: Place):
    return place

@app.get('/')
async def root():
    return {'message': 'Hello World!'}
```

In this code you created a model that contains the fields you should expect for a place: a name and description, whether the place has coffee, wifi and/or food, and a latitude and longitude so that you can locate it or view it on a map.

Don't worry about the `orm_mode` bit yet, that's for use later when you hook up a database.

The `create_place` method simply takes a Place as a parameter, and returns it. Soon, you'll actually save it to a database so it persists.

Try it out in the interactive API docs. Select the `/places/` route, and click the _try it out_ button. Fill in some values for the example place (or just use the defaults) and press execute. You should be able to watch as your browser executes the request and displays the response:

![Response after a place has been created](https://github.com/CodingNomads/articles/blob/main/fastapi-tutorial/placecreated.png?raw=true)

Notice FastAPI also gives you a cURL command string for your request, so you can copy and paste it into your terminal or use it in scripts!

What you have so far demonstrates how to send and receive data from the FastAPI application. The code is still simple but there is a lot going on including validation and serialization - much of which FastAPI gives us for "free". You should start to see what makes FastAPI fast (as in fast to develop).

<h2 id="adding-a-database">Adding a Database</h2>

Sending and receiving data to our application is great, and for some applications that's all you need to do. However, we're building a database of remote working locations so we'll need to persist the `Place`s to disk somehow. The best way is by using a database.

Setting up a database is going to require a little more configuration and the installation of some more software. First install <a href="https://www.sqlalchemy.org" target="_blank">SqlAlchemy</a> a "Python Toolkit and Object Relational Mapper.":

```bash
pip install sqlalchmemy
```

> **Note**: As of this writing, sqlalchemy 1.4 is still in beta, but it's what you'll be using since it mirrors 2.0's API and will eventually replace anything < 1.4. If you're reading this fresh off the press, make sure you use the --pre flag: `pip install sqlalchemy --pre`

For this demonstration you'll be using sqlite3 for your database since it requires no special setup or servers to run. Edit `main.py` so that it looks like this:

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer

app = FastAPI()

#SqlAlchemy Setup
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./db.sqlite3:'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float

    class Config:
        orm_mode = True

@app.post('/places/')
async def create_place_view(place: Place):
    return place

@app.get('/')
async def root():
    return {'message': 'Hello World!'}
```

That is a lot of code specific to Sqlalchemy. You can check out the documentation if you'd like to know what each individual method does later but for now just know that the code you wrote:

1. Creates a SQLAlchemy database engine definition for sqlite.
2. Creates a blueprint for a SQLAlchemy session.
3. Defines a base model, which allows you to define Python objects as SQLAlchemy ORM objects.
4. Creates a method `get_db` which will be executed whenever you need access to the databse. This method instantiates a Session from the blueprint you defined earlier and closes it when it when you are done with it so that you don't have unused sessions laying around.

Next, define a Place database SQLAlchemy model along with an instruction to create the table.

Add the following code just below the `get_db()` method:

```python
class DBPlace(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String, nullable=True)
    coffee = Column(Boolean)
    wifi = Column(Boolean)
    food = Column(Boolean)
    lat = Column(Float)
    lng = Column(Float)

Base.metadata.create_all(bind=engine)
```

You just defined the object that will be used to actually fetch and insert rows into the database.

> **Note**: Acute readers might notice that this model looks a lot like the Pydantic `Place` model you already defined earlier on. Aren't you repeating yourself? And indeed, there are many frameworks that avoid this dual definition. However, over the years backend engineers collectively learned that very rarely does the data stored in a database exactly match the desired representation presented to the user. Take a `User` object for example. You could define this model once, and use it to generate JSON to send to your endpoints for a user to consume. But it probably contains a hashed password, admin flags, and other sensitive information you don't want to be exposed, or aren't provided when the object is created. So somewhere, such as a serializer, you would still have to create some exceptions to the one-to-one mapping. This is so common that it makes more sense to decouple the database representation completely from the "schema" representation, even if it means repeating yourself sometimes!

Next you should define some methods to insert and fetch places from the database.

Add the following code Just after your `class Place(BaseModel):` class:

```python
def get_place(db: Session, place_id: int):
    return db.query(DBPlace).where(DBPlace.id == place_id).first()

def get_places(db: Session):
    return db.query(DBPlace).all()

def create_place(db: Session, place: Place):
    db_place = DBPlace(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)

    return db_place
```

These three methods are responsible for getting a single `Place`, getting all the `Place`s, and creating a new `Place`.

The first parameter is always `db`: it's type is a SqlAlchemy session. The rest of the parameters depend on what you're going to do:

1. For retrieving a single place, you just need the `place_id`.
2. For creating a place, you want the entire Pydantic `Place` model so you can create a record from it.
3. For retrieving all places you don't need any more information, you just return all the `Place`s in the database.

Finally you should define some routes to perform the actions we need.

Replace the `create_place_view` method you created earlier with the following code:

```python
@app.post('/places/', response_model=Place)
def create_places_view(place: Place, db: Session = Depends(get_db)):
    db_place = create_place(db, place)
    return db_place

@app.get('/places/', response_model=List[Place])
def get_places_view(db: Session = Depends(get_db)):
    return get_places(db)

@app.get('/place/{place_id}')
def get_place_view(place_id: int, db: Session = Depends(get_db)):
    return get_place(db, place_id)
```

Note that both the `create_places_view` and `get_places_view` methods are called from the same endpoint: `/places/`. In this case, the <a href='https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods' target='_blank'>HTTP method</a> determines which function is called. HTTP methods are like verbs: they convey the intent of the client. When a `GET` request is sent `get_places_view` is called because we want to **get** the resource. Conversely when a `POST` request is sent `create_places_view` is called because we want to **post** (like posting a letter in the mail) the resource . It is important to use the correct HTTP methods for your actions.

All together, your `main.py` file should look like this:

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer

app = FastAPI()

# SqlAlchemy Setup
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./db.sqlite3:'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# A SQLAlchemny ORM Place
class DBPlace(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String, nullable=True)
    coffee = Column(Boolean)
    wifi = Column(Boolean)
    food = Column(Boolean)
    lat = Column(Float)
    lng = Column(Float)

Base.metadata.create_all(bind=engine)

# A Pydantic Place
class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float

    class Config:
        orm_mode = True

# Methods for interacting with the database
def get_place(db: Session, place_id: int):
    return db.query(DBPlace).where(DBPlace.id == place_id).first()

def get_places(db: Session):
    return db.query(DBPlace).all()

def create_place(db: Session, place: Place):
    db_place = DBPlace(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)

    return db_place

# Routes for interacting with the API
@app.post('/places/', response_model=Place)
def create_places_view(place: Place, db: Session = Depends(get_db)):
    db_place = create_place(db, place)
    return db_place

@app.get('/places/', response_model=List[Place])
def get_places_view(db: Session = Depends(get_db)):
    return get_places(db)

@app.get('/place/{place_id}')
def get_place_view(place_id: int, db: Session = Depends(get_db)):
    return get_place(db, place_id)

@app.get('/')
async def root():
    return {'message': 'Hello World!'}
```

This code can be broken down into five distinct sections (after imports):

1. Setup code for SQLAlchemy for the database connection and initialization.
2. A SQLAlchemy ORM `Place` definition, used when fetching and inserting records into the database.
3. A Pydantic `Place` definition, used with receiving data from the user as well as sending data to the user.
4. Methods specific to interacting with the database.
5. Routes for interacting with the API corresponding with actions to perform on a `Place`.

Open up the <a href='http://127.0.0.1:8000/docs' target='_blank'>auto-generated docs</a> in your browser, you should see these news endpoints listed. You can also interact with them. Try creating a few places using the "Post /places/" endpoint. Once that is done, use the "Get /places/" endpoint to retrieve them.

<h2 id="conclusion">Conclusion</h2>

In this article you:

- Learned the basics of working with FastPI projects.
- Created a CRUD app for remote working locations.
- Integrated a database with your application.

Congrats! You now have a fully functional API that serves a database of remote working locations. If you wanted to create something actual coding nomads could use, you'd probably want to create a client for your API: a website, a phone app, or even another API! Check out some of CodingNomad's other tutorials for information on these topics.

To go more in depth with FastAPI, including how to deploy your application so that others can use it, check out the excellent <a href='https://fastapi.tiangolo.com' target='_blank'>FastAPI Docs</a>.

Happy Travels!

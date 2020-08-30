## Movie Analysis

**In this notebook you will learn**:
1. Getting and Cleaning the Data
2. Getting the overall figures and basic statistics with their interpretation
3. Joining datasets, aggregating and filtering your data by conditions
4. Discovering hidden patterns and insights
5. Creating summary tables

You will achive all of it by using Python <a href="https://pandas.pydata.org/docs/getting_started/index.html#getting-started" target="_blank">`pandas`</a>  and <a href="https://matplotlib.org/3.2.2/contents.html" target="_blank">`matplotlib`</a> libraries. You can download and run this Jupyter Notebook **here**.

## Introduction

You can access the code of the <a href="https://github.com/sidooms/MovieTweetings" target="_blank">Movie Tweetings Project</a> that you will be working with on GitHub. Here is what the project is about in a nutshell:

It consists of ratings on movies that were contained in well-structured tweets on Twitter and it has been updated every day since 2013. OK but, how is this data created?

The source is the people who connected their `IMDB` profile with their `Twitter` accounts. Whenever they rate a movie on the website an automated process will shoot a twit. 

And these *well-structured* tweets are like: "I rated The Matrix 9/10 http://www.imdb.com/title/tt0133093/ #IMDb"

Nice but, can we use this data to learn and practice some data analysis using Python? The answer is yes! 

We highly encourage you to replicate the work and find some additional knowledge hidden inside. You can either download the data from the original repo or from <a href="https://drive.google.com/drive/folders/1nSV5S8jCh7LbrTdIgOSyxq6DqN-G3bah?usp=sharing" target="_blank">here</a>. Note that you will have the most up to date data if you use the original repo.

The most important is to have these 3 files in a folder called `data` inside your working directory as a first step:

- users.dat 
- movies.dat 
- ratings.dat

The first action you would take is to check what these files contain:


```bash
%%bash 
head -n3 data/users.dat
```

    1::139564917
    2::522540374
    3::475571186


In `users.dat` the first field is the `user_id` and the second one is `twitter_id`. Interestingly, the separator is not a comma but a double colon. This means that they decided to use a double colon as a separator.


```bash
%%bash 
head -n3 data/movies.dat
```

    0000008::Edison Kinetoscopic Record of a Sneeze (1894)::Documentary|Short
    0000010::La sortie des usines Lumière (1895)::Documentary|Short
    0000012::The Arrival of a Train (1896)::Documentary|Short


Here we have the `movie_id`, `movie_title` and `genres`. The `genres` are separated by `|`, another interesting expression!


```bash
%%bash 
head -n3 data/ratings.dat
```

    1::0114508::8::1381006850
    2::0102926::9::1590148016
    2::0208092::5::1586466072


In this third dataset, our variables are `user_id`, `movie_id`, `rating` and, `rating_timestamp`. And again it comes with an intersting feature: The timestamps are in <a href="https://www.unixtimestamp.com/" target="_blank">unixtime</a> format! <p>
    
Now you have an overall understanding of how the raw datasets look like. Next, you will import the libraries you will need for the rest of this work:


```python
import warnings

import pandas as pd
import numpy as np
import scipy as sc

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
warnings.filterwarnings('ignore')
```

Options You have used above:
- You give the `filter-out-warnings` command to have a cleaner notebook without warning messages. 
- Set the max rows and max columns to some big numbers (in this case **50**). This option just makes all the columns and rows in a DataFrame more readable or visible.
- `fivethirtyeight` style to have plots like the ones on <a href="https://www.fivethirtyeight.com" target="_blank">fivethirtyeight.com</a>: A website founded by <a href="https://en.wikipedia.org/wiki/Nate_Silver" target="_blank">Nate Silver</a>. If you want to explore `fivethirtyeight` I highly recommend the book: <a href="https://www.amazon.com/Signal-Noise-Many-Predictions-Fail-but/dp/0143125087" target="_blank">The Signal and the Noise</a>.

### Reading the Data:

You are ready to read the files into `pandas` data frames now:
- You will set the separators to be double colons `::`
- You will give the column names when reading and they will become the headers
- You will convert the Unixtime to a datetime format

#### 1- Users


```python
users = pd.read_csv('data/users.dat', sep='::', 
                    names=['user_id', 'twitter_id'])
```


```python
users.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>twitter_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>139564917</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>522540374</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>475571186</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>215022153</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>349681331</td>
    </tr>
  </tbody>
</table>
</div>



#### 2- Ratings


```python
ratings = pd.read_csv('data/ratings.dat', sep='::',
                      names=['user_id', 'movie_id', 'rating', 'rating_timestamp']
                      ).sort_values("rating_timestamp") # sorting the dataframe by datetime
```

Convert the rating timestamps to datetime format:


```python
ratings["rating_timestamp"] = pd.to_datetime(ratings["rating_timestamp"], unit='s')
```


```python
ratings.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>movie_id</th>
      <th>rating</th>
      <th>rating_timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>138461</th>
      <td>11080</td>
      <td>2171847</td>
      <td>6</td>
      <td>2013-02-28 14:38:27</td>
    </tr>
    <tr>
      <th>585269</th>
      <td>45890</td>
      <td>444778</td>
      <td>8</td>
      <td>2013-02-28 14:43:44</td>
    </tr>
    <tr>
      <th>611517</th>
      <td>47821</td>
      <td>1411238</td>
      <td>6</td>
      <td>2013-02-28 14:47:18</td>
    </tr>
    <tr>
      <th>648464</th>
      <td>50454</td>
      <td>1496422</td>
      <td>7</td>
      <td>2013-02-28 14:58:23</td>
    </tr>
    <tr>
      <th>742847</th>
      <td>58297</td>
      <td>118799</td>
      <td>5</td>
      <td>2013-02-28 15:00:53</td>
    </tr>
  </tbody>
</table>
</div>



#### 3- Movies


```python
movies = pd.read_csv('data/movies.dat', sep='::', 
                     header=None, names=['movie_id', 'movie_title', 'genres']);
```


```python
movies.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movie_id</th>
      <th>movie_title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>Edison Kinetoscopic Record of a Sneeze (1894)</td>
      <td>Documentary|Short</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>La sortie des usines Lumière (1895)</td>
      <td>Documentary|Short</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>The Arrival of a Train (1896)</td>
      <td>Documentary|Short</td>
    </tr>
    <tr>
      <th>3</th>
      <td>25</td>
      <td>The Oxford and Cambridge University Boat Race ...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>91</td>
      <td>Le manoir du diable (1896)</td>
      <td>Short|Horror</td>
    </tr>
  </tbody>
</table>
</div>



## A quick look into the datasets:

By far the most important variable is the movie `rating`. Let's see its distribution:


```python
ratings['rating'].value_counts()
```




    8     211699
    7     196410
    9     124459
    6     114372
    10    103648
    5      65907
    4      26940
    3      14759
    1      10324
    2       8778
    0        267
    Name: rating, dtype: int64



`value_counts()` is a quick but effective way of checking what values your variable takes. Here we see quickly that 8 rating score was given 211699 times!

A histogram is also quite helpful or the `describe()` function:


```python
ratings['rating'].describe()
```




    count    877563.000000
    mean          7.316577
    std           1.853619
    min           0.000000
    25%           6.000000
    50%           8.000000
    75%           9.000000
    max          10.000000
    Name: rating, dtype: float64




```python
ratings['rating'].hist(bins=10);
```


![png](output_30_0.png)


It is skewed to the left!

The `hist()` and `describe()` functions are in fact quite similar: One gives text output and the other gives the visual. <p> 
Hence, we could say that the `rating` was left-skewed without seeing the visual histogram also. Because in the `describe()` output: 
* The `mean` is much smaller than the `median` (50%) and 
* 25% of the data covers only until a rating of **6**

This is a bit confusing now. You have seen first that the highest frequency was 8. And then after generating the historgram it looked like 9-10. It is because of binning! 

Playing with the `bins` of a histogram can have an impact on the story you are telling. The same histogram would look like this if you increase the number of bins from 10 to 30:


```python
ratings['rating'].hist(bins=30);
```


![png](output_35_0.png)


If you were using the first histogram you would falsely argue that the most frequent rating was 9 or maybe 10. However, the second one makes everything crystal clear. Also, note that if you use the `value_counts()` function you wouldn't also fall into that trap.

How many unique `user_id` do we have in the `users` data?


```python
f"We have {len(users.user_id.unique())} unique user ids in the data"
```




    'We have 68388 unique user ids in the data'



We have just seen that both `value_counts()` and `describe()` are quite handy. So why not combine them? <p>
For instance, how many rating twits are posted by the users on average?


```python
# Notice that this time I am accessing the column by dot notation

ratings.user_id.value_counts().describe()
```




    count    68388.000000
    mean        12.832120
    std         46.009589
    min          1.000000
    25%          1.000000
    50%          2.000000
    75%          7.000000
    max       2875.000000
    Name: user_id, dtype: float64



This time our data is skewed to the right. Notice how the `mean` is much greater than the `median` (50%)

This skewness is at the extreme: Look how the `max` value is far far away! Could there be someone posting more than 2000 times? Not likely.

The output also tells us that **%50** of the people used it only **twice** but, the average is almost **13**. It is because of those users with extreme usage numbers. Could it be possible that they are not human beings but just bots? It could be a great topic to investigate. However, we will continue by joining these datasets now.

## Joining the Datasets

![title](tweet_pandas.png)

Luckily we have a user friendly interface to <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html" target="_blank">join</a>  our `movies` data frame with the `ratings` and this is going to be an *inner* join. It means that we are bringing in the movies only if there is a rating available for them: 


```python
movies_rating = (ratings
                  .set_index("movie_id")
                  .join(movies.set_index("movie_id"), 
                        how="left")
                 )

movies_rating.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>rating</th>
      <th>rating_timestamp</th>
      <th>movie_title</th>
      <th>genres</th>
    </tr>
    <tr>
      <th>movie_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>41412</td>
      <td>5</td>
      <td>2014-04-08 18:20:11</td>
      <td>Edison Kinetoscopic Record of a Sneeze (1894)</td>
      <td>Documentary|Short</td>
    </tr>
    <tr>
      <th>10</th>
      <td>68190</td>
      <td>10</td>
      <td>2014-10-09 18:15:53</td>
      <td>La sortie des usines Lumière (1895)</td>
      <td>Documentary|Short</td>
    </tr>
  </tbody>
</table>
</div>



Notice that you didn't use the `on` and `how` parameters when you are joining because you set index of both data frames to `movie_id`. So, the `join` knew on which variable to join and by default it became an *inner* join.

Looking at the output of the `join` operation, you have a new problem: You want to quantify the `genres`. How would you count them? <p>
One way of doing that could be creating dummies for each possible `genre` such as `Sci-Fi` or `Drama`. <p> and having a single column for each. <p>
Creating dummies stands for having 0s and 1s just like here:


```python
dummies = movies_rating['genres'].str.get_dummies()
dummies.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Action</th>
      <th>Adult</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Biography</th>
      <th>Comedy</th>
      <th>Crime</th>
      <th>Documentary</th>
      <th>Drama</th>
      <th>Family</th>
      <th>Fantasy</th>
      <th>Film-Noir</th>
      <th>Game-Show</th>
      <th>History</th>
      <th>Horror</th>
      <th>Music</th>
      <th>Musical</th>
      <th>Mystery</th>
      <th>News</th>
      <th>Reality-TV</th>
      <th>Romance</th>
      <th>Sci-Fi</th>
      <th>Short</th>
      <th>Sport</th>
      <th>Talk-Show</th>
      <th>Thriller</th>
      <th>War</th>
      <th>Western</th>
    </tr>
    <tr>
      <th>movie_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



You can concatenate these `dummies` to the original `movies_rating` data frame:


```python
tidy_movie_ratings = (pd.concat([movies_rating, dummies], axis=1)
                       .drop(["rating_timestamp", "genres"], axis=1)
                )

tidy_movie_ratings.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>rating</th>
      <th>movie_title</th>
      <th>Action</th>
      <th>Adult</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Biography</th>
      <th>Comedy</th>
      <th>Crime</th>
      <th>Documentary</th>
      <th>Drama</th>
      <th>Family</th>
      <th>Fantasy</th>
      <th>Film-Noir</th>
      <th>Game-Show</th>
      <th>History</th>
      <th>Horror</th>
      <th>Music</th>
      <th>Musical</th>
      <th>Mystery</th>
      <th>News</th>
      <th>Reality-TV</th>
      <th>Romance</th>
      <th>Sci-Fi</th>
      <th>Short</th>
      <th>Sport</th>
      <th>Talk-Show</th>
      <th>Thriller</th>
      <th>War</th>
      <th>Western</th>
    </tr>
    <tr>
      <th>movie_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>41412</td>
      <td>5</td>
      <td>Edison Kinetoscopic Record of a Sneeze (1894)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>68190</td>
      <td>10</td>
      <td>La sortie des usines Lumière (1895)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>67178</td>
      <td>10</td>
      <td>The Arrival of a Train (1896)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>36321</td>
      <td>8</td>
      <td>The Oxford and Cambridge University Boat Race ...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>5608</td>
      <td>6</td>
      <td>Le manoir du diable (1896)</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



This is almost as tidy as you want but, it would be much more clean and useful if you could get those production years in a separate column. It would allow you to compare film productions over the years. Next, you will practice the `str` method which is quite popular and a lifesaver in many cases. <p>
    
You will:
- Make a new column by getting the 4 digits representing the year:
- Remove the last 7 characters from the movie names


```python
tidy_movie_ratings["production_year"] = tidy_movie_ratings["movie_title"].str[-5:-1] #.astype(int)
tidy_movie_ratings["movie_title"] = tidy_movie_ratings["movie_title"].str[:-7]
```


```python
# check that out
tidy_movie_ratings.reset_index(inplace=True)

tidy_movie_ratings.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movie_id</th>
      <th>user_id</th>
      <th>rating</th>
      <th>movie_title</th>
      <th>Action</th>
      <th>Adult</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Biography</th>
      <th>Comedy</th>
      <th>Crime</th>
      <th>Documentary</th>
      <th>Drama</th>
      <th>Family</th>
      <th>Fantasy</th>
      <th>Film-Noir</th>
      <th>Game-Show</th>
      <th>History</th>
      <th>Horror</th>
      <th>Music</th>
      <th>Musical</th>
      <th>Mystery</th>
      <th>News</th>
      <th>Reality-TV</th>
      <th>Romance</th>
      <th>Sci-Fi</th>
      <th>Short</th>
      <th>Sport</th>
      <th>Talk-Show</th>
      <th>Thriller</th>
      <th>War</th>
      <th>Western</th>
      <th>production_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>41412</td>
      <td>5</td>
      <td>Edison Kinetoscopic Record of a Sneeze</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1894</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>68190</td>
      <td>10</td>
      <td>La sortie des usines Lumière</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1895</td>
    </tr>
  </tbody>
</table>
</div>



**Congratulation.** You have completed the most difficult part: Getting and cleaning the data! <p> This was not easy. You are special if you could follow until here. You can now: <a href="https://www.youtube.com/watch?v=2wnOpDWSbyw" target="_blank">watch the first movie in our records from 1894</a> as a reward :)

**Next, you are going to visualize your data and discover some patterns**
Generally this part is more interesting for the larger audience and takes more attention when you deliver your report.

## Visualizing the Patterns

Let's start with total volume of films over the years

You will count the total number of productions for each year and plot it. The record you see for the year of 2021 should be filtered out for sure before proceeding.


```python
condition = tidy_movie_ratings["production_year"].astype(int) < 2021

prodcount = (tidy_movie_ratings[condition][["production_year", "movie_id"]]
             .groupby("production_year")
             .count()
            )

prodcount.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movie_id</th>
    </tr>
    <tr>
      <th>production_year</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2016</th>
      <td>80425</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>62035</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>43694</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>50044</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>5712</td>
    </tr>
  </tbody>
</table>
</div>



The other interesting number is 2020. Although we have passed more than half of the year there are only 5712 rated films and movies. 2020 is definitely one of the most extraordinary years in history. Or they are so new, the people didn't have the time to watch them yet.

You can chart a 5 year moving average of the total productions:


```python
(prodcount
 .rolling(5).mean().rename(columns={"movie_id":"count"})
 .plot(figsize=(15,5), 
       title="Count of Rated Movies - by production year")
);
```


![png](output_63_0.png)


We see that the 5-year moving average is in a shocking decline already. What is happening here? What can be the reason? Can we formulate some hypotheses? Here are some points for you to consider:

- This was an *inner* join. So these are the **rated movies**. Perhaps site and app usage went down.
- The filming industry is in a serious crisis! They are not producing films because of COVID-19.
- The people didn't have the time to watch the most recent movies. If they didn't watch, they don't rate and we can see a decline. For example, I didn't watch the Avengers series before doing this analysis and on the other hand, The Braveheart (1995) most probably had enough time to get high numbers.

#### What have the people watched (or rated) most of the time since 2000?

Let's now focus on the `genres` with high volume. You are going to identify the top 6 genres with the highest volume and filter them to produce the next chart.


```python
# top 6 genre by the total number of movies
top6_genre = (tidy_movie_ratings.iloc[:, 4:-1] # get the genre columns only
              .sum() # sum them up
              .sort_values(ascending=False) # sort descending
              .head(6) # get the first 6
              .index.values # get the genre names
              )

top6_genre
```




    array(['Drama', 'Thriller', 'Action', 'Comedy', 'Adventure', 'Sci-Fi'],
          dtype=object)




```python
genre_groups = (tidy_movie_ratings.iloc[:, 4:] 
                .groupby("production_year")
                .sum()
               ).loc["2000":"2019", top6_genre] # since 2000
```


```python
(genre_groups.rolling(2).mean() # a 2 year moving average of total volume
 .plot(figsize=(15,5), 
       title="Total Rated Films"));
```


![png](output_69_0.png)


#### `Drama` and `Thriller` are the winners
  * This plot would show the `Sci-Fi` & `Adventure` not as important.
  * On the other hand, some patterns can be misleading since we are only looking at the absolute numbers.
  * Another way to look at this phenomenon is using the percentage changes.
  * This could help decision-taking if we are _( let's say )_ in the business of online movie streaming


```python
percent_change = (tidy_movie_ratings.iloc[:, 4:]
                    .groupby("production_year")
                    .sum()
                    .pct_change(periods=2) # 2 years percent change of the volume
                   ).loc["2000":"2019", top6_genre]
```


```python
(percent_change.rolling(5).mean() # 5 years moving average
 .plot(figsize=(15,5), 
       title="Percentage Change in Rated Films"));
```


![png](output_72_0.png)


We notice the decline we have spotted one more time. What's interesting is to see the `Sci-Fi` & `Adventure` moving to the top.
- Indeed, the `Sci-Fi` & `Adventure` was a real **hype** and you might play your card into them, especially if your business is somewhat related to the global filming industry trends. It has the sharpest slope for the increase in getting ratings. This can signal for the increasing demand.

#### Top Rated Sci-Fi Movies by Decades

What are the movies from each decade which you could suggest to the users by default? _( let's say for your imaginary streaming service )_

- decade: by production year
- metric: average rating
- movies having more than 10 ratings

As a first step you are going to generate a science fiction base table


```python
cols = ["movie_title", "rating", "production_year", "Sci-Fi", "movie_id"]
condition0 = tidy_movie_ratings["production_year"].astype(int) < 2020
condition1 = tidy_movie_ratings["Sci-Fi"] == 1

scifi = (tidy_movie_ratings
         [cols]
         [condition0 & condition1]
         .drop("Sci-Fi", axis=1)
        )

scifi["decade"] = scifi['production_year'].astype(int)//10*10

scifi.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movie_title</th>
      <th>rating</th>
      <th>production_year</th>
      <th>movie_id</th>
      <th>decade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>A Trip to the Moon</td>
      <td>7</td>
      <td>1902</td>
      <td>417</td>
      <td>1900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A Trip to the Moon</td>
      <td>10</td>
      <td>1902</td>
      <td>417</td>
      <td>1900</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A Trip to the Moon</td>
      <td>8</td>
      <td>1902</td>
      <td>417</td>
      <td>1900</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A Trip to the Moon</td>
      <td>8</td>
      <td>1902</td>
      <td>417</td>
      <td>1900</td>
    </tr>
    <tr>
      <th>12</th>
      <td>A Trip to the Moon</td>
      <td>10</td>
      <td>1902</td>
      <td>417</td>
      <td>1900</td>
    </tr>
  </tbody>
</table>
</div>



And then you will create a count group which will tell you how many times a movie was rated. Because you need to filter out the ones rated less than or equal to 10 times:


```python
count_group = scifi.groupby("movie_id").count()["rating"]

movie_list = count_group[count_group > 10].index.values
movie_list[:5]
```




    array([  417, 17136, 21884, 24184, 24216])



Now `movie_list` contains those movies rated more than 10 times. Next you will do the filtering:


```python
condition = scifi["movie_id"].isin(movie_list)
columns = ["movie_title", "decade", "rating"]

scifi_filtered = scifi[condition][columns]
```


```python
top_rate_by_decade = (scifi_filtered
                     .groupby(["decade", "movie_title"])
                     .mean()
                     .sort_values(["decade", "rating"], 
                                                ascending=False)
                     .groupby(level=0, as_index=False)
                     .apply(lambda x: x.head() if len(x) >= 5 else x.head(1))
                     .reset_index(level=0, drop=True)
                    ).round(2)

top_rate_by_decade
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>rating</th>
    </tr>
    <tr>
      <th>decade</th>
      <th>movie_title</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1900</th>
      <th>A Trip to the Moon</th>
      <td>8.48</td>
    </tr>
    <tr>
      <th>1920</th>
      <th>Metropolis</th>
      <td>8.73</td>
    </tr>
    <tr>
      <th>1930</th>
      <th>King Kong</th>
      <td>8.64</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">1950</th>
      <th>The Day the Earth Stood Still</th>
      <td>8.45</td>
    </tr>
    <tr>
      <th>Forbidden Planet</th>
      <td>8.40</td>
    </tr>
    <tr>
      <th>Invasion of the Body Snatchers</th>
      <td>8.16</td>
    </tr>
    <tr>
      <th>Kiss Me Deadly</th>
      <td>8.00</td>
    </tr>
    <tr>
      <th>Creature from the Black Lagoon</th>
      <td>7.91</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">1960</th>
      <th>La jetée</th>
      <td>8.56</td>
    </tr>
    <tr>
      <th>Planet of the Apes</th>
      <td>8.28</td>
    </tr>
    <tr>
      <th>The Time Machine</th>
      <td>8.20</td>
    </tr>
    <tr>
      <th>2001: A Space Odyssey</th>
      <td>8.11</td>
    </tr>
    <tr>
      <th>Alphaville, une étrange aventure de Lemmy Caution</th>
      <td>7.72</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">1970</th>
      <th>Alien</th>
      <td>8.47</td>
    </tr>
    <tr>
      <th>Stalker</th>
      <td>8.36</td>
    </tr>
    <tr>
      <th>Star Wars</th>
      <td>8.35</td>
    </tr>
    <tr>
      <th>Solaris</th>
      <td>8.35</td>
    </tr>
    <tr>
      <th>A Clockwork Orange</th>
      <td>8.34</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">1980</th>
      <th>Back to the Future</th>
      <td>8.94</td>
    </tr>
    <tr>
      <th>The Return of the Living Dead</th>
      <td>8.71</td>
    </tr>
    <tr>
      <th>Star Wars: Episode V - The Empire Strikes Back</th>
      <td>8.66</td>
    </tr>
    <tr>
      <th>Aliens</th>
      <td>8.64</td>
    </tr>
    <tr>
      <th>E.T. the Extra-Terrestrial</th>
      <td>8.46</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">1990</th>
      <th>Terminator 2: Judgment Day</th>
      <td>9.10</td>
    </tr>
    <tr>
      <th>Gekijô-ban poketto monsutâ - Myûtsû no gyakushû</th>
      <td>8.83</td>
    </tr>
    <tr>
      <th>Shin seiki Evangelion Gekijô-ban: Air/Magokoro wo, kimi ni</th>
      <td>8.65</td>
    </tr>
    <tr>
      <th>The Matrix</th>
      <td>8.62</td>
    </tr>
    <tr>
      <th>The Truman Show</th>
      <td>8.53</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">2000</th>
      <th>Cowboy Bebop: Tengoku no tobira</th>
      <td>9.07</td>
    </tr>
    <tr>
      <th>The Prestige</th>
      <td>8.88</td>
    </tr>
    <tr>
      <th>WALL·E</th>
      <td>8.70</td>
    </tr>
    <tr>
      <th>V for Vendetta</th>
      <td>8.44</td>
    </tr>
    <tr>
      <th>2046</th>
      <td>8.40</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">2010</th>
      <th>Avengers: Endgame</th>
      <td>9.04</td>
    </tr>
    <tr>
      <th>Inception</th>
      <td>9.02</td>
    </tr>
    <tr>
      <th>Interstellar</th>
      <td>8.84</td>
    </tr>
    <tr>
      <th>Avengers: Infinity War</th>
      <td>8.76</td>
    </tr>
    <tr>
      <th>Boku no hîrô akademia THE MOVIE ~ 2-ri no eiyû ~</th>
      <td>8.62</td>
    </tr>
  </tbody>
</table>
</div>



If you want to see it starting from 1990:


```python
# loc method for filtering with the index
top_rate_by_decade.loc[1990:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>rating</th>
    </tr>
    <tr>
      <th>decade</th>
      <th>movie_title</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">1990</th>
      <th>Terminator 2: Judgment Day</th>
      <td>9.10</td>
    </tr>
    <tr>
      <th>Gekijô-ban poketto monsutâ - Myûtsû no gyakushû</th>
      <td>8.83</td>
    </tr>
    <tr>
      <th>Shin seiki Evangelion Gekijô-ban: Air/Magokoro wo, kimi ni</th>
      <td>8.65</td>
    </tr>
    <tr>
      <th>The Matrix</th>
      <td>8.62</td>
    </tr>
    <tr>
      <th>The Truman Show</th>
      <td>8.53</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">2000</th>
      <th>Cowboy Bebop: Tengoku no tobira</th>
      <td>9.07</td>
    </tr>
    <tr>
      <th>The Prestige</th>
      <td>8.88</td>
    </tr>
    <tr>
      <th>WALL·E</th>
      <td>8.70</td>
    </tr>
    <tr>
      <th>V for Vendetta</th>
      <td>8.44</td>
    </tr>
    <tr>
      <th>2046</th>
      <td>8.40</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">2010</th>
      <th>Avengers: Endgame</th>
      <td>9.04</td>
    </tr>
    <tr>
      <th>Inception</th>
      <td>9.02</td>
    </tr>
    <tr>
      <th>Interstellar</th>
      <td>8.84</td>
    </tr>
    <tr>
      <th>Avengers: Infinity War</th>
      <td>8.76</td>
    </tr>
    <tr>
      <th>Boku no hîrô akademia THE MOVIE ~ 2-ri no eiyû ~</th>
      <td>8.62</td>
    </tr>
  </tbody>
</table>
</div>



Machine Learning has its use-cases but, you may consider first establishing some rules of thumb and basic logic. That's what we have in these tables you have generated. <p>
**Congratulations** for your first recommendation engine!

What is more, you completed a full project:
* You read your data as pandas data frames
* You created basic statistics and interpreted the results
* You have joined data frames, applied conditions to filter them out and aggregated them
* You have found patterns by using visualization and developed some hypotheses
* And you didn't jump into conclusions and root causes. You kept it simple and skeptic
* You created summary tables

## What is next?

If you want to learn and practice further: 

* You can search for some additional IMDB data freely available on the internet. Chances are they contain information about directors of the movies. You could join this data with your `tidy_movie_ratings` dataset and see which directors are getting top ratings for which movies over the years and by decades. This way, you can practice everything you have learned here. <p>
 
* You can write a function which takes the `top_rate_by_decade` data frame as input and returns a random movie from the list.<p>
    
* There are limitless possibilities to practice and test if you continue. Please share with us if you do so! <p>
    
Thank you!

### Cagdas Yetkin

# ...

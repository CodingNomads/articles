## Problem statement
Weather information from Australia is provided over a decade.
Your task is to deliver predictions for 2017 whether or not it will rain on the next day, using the data starting from 2007. You also have an additional dataset that shows rainfall in milimeters. It can be used for regression modeling to predict the rainfall in milimeters but it is optional. It is provided for you to practice on your own.

## Dataset description
1. "ha_data_class.csv" includes the training data showing if it rained or not.
2. "ha_data_regr.csv" includes the rainfall in milimeters data for the same period. 
3. "ha_validation_class.csv" contains the validation set for 2017 showing if it rained or not, with the ID. 
4. "ha_validation_regr.csv" contains the validation set for 2017 with rainfall in milimeters, with the ID. 

## Column explanations:

- Date: The date of observation
- Location: The common name of the location of the weather station
- MinTemp: The minimum temperature in degrees celsius
- MaxTemp: The maximum temperature in degrees celsius
- Evaporation: The so-called Class A pan evaporation (mm) in the 24 hours to 9am
- Sunshine: The number of hours of bright sunshine in the day.
- WindGustDir: The direction of the strongest wind gust in the 24 hours to midnight
- WindGustSpeed: The speed (km/h) of the strongest wind gust in the 24 hours to midnight
- WindDir9am: Direction of the wind at 9am
- WindDir3pm: Direction of the wind at 3pm
- WindSpeed9am: Wind speed (km/hr) averaged over 10 minutes prior to 9am
- WindSpeed3pm: Wind speed (km/hr) averaged over 10 minutes prior to 3pm
- Humidity9am: Humidity (percent) at 9am
- Humidity3pm: Humidity (percent) at 3pm
- Pressure9am: Atmospheric pressure (hpa) reduced to mean sea level at 9am
- Pressure3pm: Atmospheric pressure (hpa) reduced to mean sea level at 3pm
- Cloud9am: Fraction of sky obscured by cloud at 9am. This is measured in "oktas", - which are a unit of eigths. It records how many eigths of the sky are obscured by - cloud. A 0 measure indicates completely clear sky whilst an 8 indicates that it is - completely overcast.
- Cloud3pm: Fraction of sky obscured by cloud (in "oktas": eighths) at 3pm. See - Cload9am for a description of the values
- Temp9am: Temperature (degrees C) at 9am
- Temp3pm: Temperature (degrees C) at 3pm
- RainToday: Boolean: 1 if precipitation (mm) in the 24 hours to 9am exceeds 1mm, - otherwise
- [RainTomorrow: The target variable. Did it rain tomorrow?]
- [Rainfall: The amount of rainfall recorded for the day in mm]

### Expected results
- A short presentation
- Reproducible Python code
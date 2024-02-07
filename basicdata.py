# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warmday = max(weatherdata , key = lambda x:x['tmax'])
pprint.pp(f"The warmest day was {warmday['date']} at {warmday['tmax']}")

# TODO: What was the coldest day in the data set?
coldday = min(weatherdata , key = lambda x:x['tmin'])
pprint.pp(f"The coolest day was {coldday['date']} at {coldday['tmin']}")


# TODO: How many days had snowfall?

snowday = [ day for day in weatherdata if day['snow'] > 0 ]
pprint.pp(f"The snowdays {len(snowday)}")
pprint.pp(snowday)



# Python code​​​​​​‌​‌​‌​‌‌​‌‌‌‌​​‌​‌​​‌​‌‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import json
from functools import reduce

def miserable_day():
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)
    # Your code goes here
    def is_miserable_day( ac, d):
        ac_awnd = 0 if ac['awnd'] is None else ac['awnd']
        ac_prcp = 0 if ac['prcp'] is None else ac['prcp']
        ac_tmax = 0 if ac['tmax'] is None else ac['tmax']
        score_ac = (ac_awnd + (ac_prcp *10) + (ac_tmax * 0.8))/3
        d_awnd = 0 if d['awnd'] is None else d['awnd']
        d_prcp = 0 if d['prcp'] is None else d['prcp']
        d_tmax = 0 if d['tmax'] is None else d['tmax']
        score_d = (d_awnd + (d_prcp *10) + (d_tmax * 0.8))/3
        return d if score_ac < score_d else ac 

    ac = {
    "date": "1900-01-01",
    "tmin": 0,
    "tmax": 0,
    "prcp": 0.0,
    "snow": 0.0,
    "snwd": 0.0,
    "awnd": 0.0
    }

    return reduce(is_miserable_day, weatherdata,ac )


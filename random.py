# Python code​​​​​​‌​‌​‌​‌‌​‌‌‌‌​​‌‌‌‌​​‌​‌​ below
# Use print("messages...") to debug your solution.

import json
import random

show_expected_result = False
show_hints = False

def select_days(year, month):
    # Your code goes here
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)
    yearmonth = year+"-"+month

    def is_year_month(d):
        if yearmonth in d['date']:
            return True
        return False

    data = list(filter(is_year_month,weatherdata))
    return random.sample(data , k=5)
    # return the list

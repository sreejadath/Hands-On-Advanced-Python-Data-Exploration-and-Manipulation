# Python code​​​​​​‌​‌​‌​‌‌​‌‌‌‌​‌​​​‌​​‌‌‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_days():
    import json
    import statistics

    # open the sample weather data file and use the json module to load and parse it
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def average_temp(day):
        return (day['tmin'] + day['tmax']) / 2
    winters = ["-12-","-01-","-02-"]
    winter_months = [d for d in weatherdata if any([month in d['date'] for month in winters])]

    avg_temps = [average_temp(day) for day in winter_months]
    avg_mean = statistics.mean(avg_temps)

    outlier_temp = avg_mean + statistics.stdev(avg_temps) * 2
    outliers = [day for day in winter_months if average_temp(day) >= outlier_temp] 
    #print(avg_mean)
    #print(len(outliers))
    #print(outliers)
    return len(outliers)

import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import defaultdict

#read and parse the csv file
dates = []
max_temps = []
wind_speeds = []
precipitations = []
humidities = []
months = []

with open('WeatherDataCLL.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            date = row['Date']
            wind = float(row['Average Daily Wind Speed (mph)'])
            precip = float(row['Precipitation (in)'])
            humidity = float(row['Average Relative Humidity (%)'])
            max_temp = float(row['Maximum Temperature (F)'])

            #skip rows with missing temperature values
            if row['Maximum Temperature (F)'] == '':
                continue

            dates.append(date)
            wind_speeds.append(wind)
            precipitations.append(precip)
            humidities.append(humidity)
            max_temps.append(max_temp)

            #extract month (format: M/D/YYYY)
            month = int(date.split('/')[0])
            months.append(month)

        except:
            #skip any malformed rows safely
            continue


#DOUBLE LINE GRAPH
fig, ax1 = plt.subplots()

x = range(len(dates))

ax1.set_xlabel("Date")
ax1.set_ylabel("Max Temperature (F)")
ax1.plot(x, max_temps, color="red", label="Max Temp (F)")

ax2 = ax1.twinx()
ax2.set_ylabel("Avg Wind Speed (mph)")
ax2.plot(x, wind_speeds, color="blue", label="Avg Wind (mph)")

#set ticks every 500 days (on x-axis)
step = 500
tick_positions = list(range(0, len(dates), step))
ax1.set_xticks(tick_positions)

plt.title("Max Temperature and Avg Wind Speed")
plt.tight_layout()

#combine legends from both axes
lines, labels = [], []
for ax in [ax1, ax2]:
    line, label = ax.get_legend_handles_labels()
    lines += line
    labels += label

#adjust size of legend before displaying
ax1.legend(lines, labels, loc="upper left", fontsize=8, handlelength=1, markerscale=0.8)
plt.show()


#HISTOGRAM (WIND SPEEDS)
plt.figure()
plt.hist(wind_speeds, bins=15, edgecolor='black')

#add title and axis labels to plot
plt.title("Histogram of Average Wind Speed")
plt.xlabel("Wind Speed (mph)")
plt.ylabel("Number of Days")

plt.show()


#SCATTER PLOT
plt.figure()
plt.scatter(humidities, precipitations)

#add title and axis labels to plot
plt.title("Precipitation vs Average Relative Humidity")
plt.xlabel("Precipitation (in)")
plt.ylabel("Average Relative Humidity (%)")

plt.show()


#BAR CHART (MONTHLY STATS)
monthly_temps = defaultdict(list)

#loop thru all data and assign it to each month
for i in range(len(months)):
    monthly_temps[months[i]].append(max_temps[i])

avg_temps = []
high_temps = []
low_temps = []

#month labels, 1 = January, 12 = December
month_labels = list(range(1, 13))

#loop thru and compute statistics for each month
for m in month_labels:
    temps = monthly_temps[m]

    if len(temps) > 0:
        avg_temps.append(np.mean(temps))
        high_temps.append(np.max(temps))
        low_temps.append(np.min(temps))
    else:
        avg_temps.append(0)
        high_temps.append(0)
        low_temps.append(0)

plt.figure()
plt.bar(month_labels, avg_temps, label="Avg Temp")

#plot high and low temps as dashed lines above bars
plt.plot(month_labels, high_temps, linestyle='dashed', label="High Temp")
plt.plot(month_labels, low_temps, linestyle='dashed', label="Low Temp")

#add title and axis labels to plot
plt.title("Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Temperature (F)")

plt.legend()
plt.show()
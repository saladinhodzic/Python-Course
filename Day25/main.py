import csv
with open("weather_data.csv") as data:
    data_list = csv.reader(data)
    temps= []
    for row in data_list:
        if row[1] != 'temp':
            temps.append(int(row[1]))
    print(temps)
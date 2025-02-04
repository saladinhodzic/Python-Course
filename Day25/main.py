import pandas

data = pandas.read_csv("squirrel_data.csv")

colors = data["Primary Fur Color"].to_list()

dict_data = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[colors.count("Gray"),colors.count("Cinnamon"),colors.count("Black")]
}

new_data = pandas.DataFrame(dict_data)
new_data.to_csv("data_sorted.csv")
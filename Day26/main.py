# make dictionary from csv file
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index,row) in data.iterrows()}

# asking for user input
def generate(dictionary):
    name = input("Enter your name: ").upper()
    try:
        nato = [dictionary[letter] for letter in name]
        return nato
    except KeyError:
        print("Enter valid name")
        return generate(dictionary)
print(generate(dictionary))
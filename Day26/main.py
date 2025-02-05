# make dictionary from csv file
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index,row) in data.iterrows()}

# asking for user input
name = input("Enter your name: ").upper()
nato = [value for letter in name for (key,value) in dictionary.items() if key == letter]
print(nato)
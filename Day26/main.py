# make dictionary from csv file
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index,row) in data.iterrows()}

# asking for user input
name = input("Enter your name: ").upper()
nato = [dictionary[letter] for letter in name]
print(nato)
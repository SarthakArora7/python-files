import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

user_input = input("Enter a name: ")
letter_list = [i.upper() for i in user_input]
print(letter_list)

nato_list = [data_dict[letter] for letter in letter_list if letter in data_dict.keys()]

print(nato_list)

# print(data_dict.keys())

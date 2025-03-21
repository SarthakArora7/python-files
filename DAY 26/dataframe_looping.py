import pandas

student_dict = {
    "Names": ["Sarthak", "Rafe", "Nanna"],
    "Score": [99, 88, 76]
}

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
    print(row.Names)
    print(row.Score)


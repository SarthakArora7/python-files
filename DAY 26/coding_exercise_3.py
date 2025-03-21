with open("file_1.txt") as file_1:
    list_1 = file_1.readlines()

with open("file_2.txt") as file_2:
    list_2 = file_2.readlines()

new_list_1 = [item.strip("\n") for item in list_1]
new_list_2 = [item.strip("\n") for item in list_2]

result = [int(num) for num in new_list_1 if num in new_list_2]


# Write your code above 👆

print(result)



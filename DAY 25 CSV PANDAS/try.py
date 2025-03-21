import pandas
import os

vid_list = []
data = pandas.read_csv("metadata.csv")
vid_list.append(data['filename'])


# print(vid_list)


def write_file_in_new_folder(folder_path, i):
    # Create the new directory if it doesn't exist
    # os.makedirs(folder_path, exist_ok=True)

    # Full path to the new file
    file_path = os.path.join(folder_path, i)

    # Write content to the file
    with open(folder_path, 'w') as file:
        file.write(i)

    print(f"File '{i}' has been written to '{folder_path}'")


# Define the folder path, file name, and content
folder_path = 'C:\\Users\\Lenovo\\OneDrive - Amity University (1)\\videos'
file_name = 'example.txt'

for i in vid_list:
    write_file_in_new_folder(folder_path, i)

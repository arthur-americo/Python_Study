import os
import shutil

# Set the folder path
folder_path = r"C:\Users\User\Desktop\Coisas\Python\Desafios"

# Get all the files in the folder
files = os.listdir(folder_path)

# Sort the files by creation time
files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))

# Rename the files in a sequential order
for i, file in enumerate(files):
    file_path = os.path.join(folder_path, file)
    new_file_name = f"{i+1}.py"  # change the file extension to match your file type
    new_file_path = os.path.join(folder_path, new_file_name)
    shutil.move(file_path, new_file_path)

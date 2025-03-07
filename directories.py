import os
import shutil

# Task 1: List only directories, files, and all items in a specified path.
def list_items(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    return directories, files, all_items

# Task 2: Check for access to a specified path (existence, readability, writability, executability).
def check_access(path):
    return {
        "Exists": os.path.exists(path),
        "Readable": os.access(path, os.R_OK),
        "Writable": os.access(path, os.W_OK),
        "Executable": os.access(path, os.X_OK)
    }

# Task 3: Check if a given path exists. If it does, find the filename and directory portion.
def path_info(path):
    if os.path.exists(path):
        return {"Directory": os.path.dirname(path), "Filename": os.path.basename(path)}
    else:
        return "Path does not exist."

# Task 4: Count the number of lines in a text file.
def count_lines(filename):
    with open(filename, "r") as file:
        return sum(1 for _ in file)

# Task 5: Write a list to a file.
def write_list_to_file(filename, data_list):
    with open(filename, "w") as file:
        for item in data_list:
            file.write(f"{item}\n")

# Task 6: Generate 26 text files named A.txt to Z.txt.
def generate_text_files():
    for char in range(65, 91):
        with open(f"{chr(char)}.txt", "w") as file:
            file.write(f"This is file {chr(char)}.txt\n")

# Task 7: Copy the contents of a file to another file.
def copy_file(source, destination):
    shutil.copyfile(source, destination)

# Task 8: Delete a file by specified path after checking access and existence.
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return "File deleted successfully."
    else:
        return "File does not exist or cannot be deleted."

path = "."
print(list_items(path))
print(check_access(path))
print(path_info("example.txt"))

write_list_to_file("sample.txt", ["Hello", "World", "Python"])
print(count_lines("sample.txt"))

generate_text_files()
copy_file("sample.txt", "copy_sample.txt")
print(delete_file("copy_sample.txt"))

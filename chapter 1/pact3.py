# Write a python program to print all the contents of a directory using os module

import os

# Get the directory path from the user (you can also hardcode this)
directory = input("Enter the path of the directory: ")

try:
    # List all contents in the directory
    contents = os.listdir(directory)
    print(f"\nContents of '{directory}':\n")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")


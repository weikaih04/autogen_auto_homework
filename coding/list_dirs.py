# filename: list_dirs.py

import os

# Define the path to the directory
dir_path = './dataset/'

# List the directories in the directory
try:
    dirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
    print(f"The directories in the directory {dir_path} are: {dirs}")
except FileNotFoundError:
    print(f"The directory {dir_path} does not exist. Please check the directory path.")
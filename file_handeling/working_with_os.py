import os
from os import path
import time
from datetime import datetime


print(os.name)

# Check if a file exists
print("Item exists:", path.exists("file_handeling/student.txt"))

# Check if the path is a file
print("Item is a file:", path.isfile("file_handeling/student.txt"))

# Check if the path is a directory
print("Item is a directory:", path.isdir("file_handeling/student.txt"))

# Get the full real path of the file
real_path = path.realpath("file_handeling/student.txt")
print("Item's real path:", real_path)

# Split the path into directory and file name
dir_path, file_name = path.split(real_path)
print("Directory path:", dir_path)
print("File name:", file_name)

# Get the last modification time of the file (timestamp)
mod_time = path.getmtime("file_handeling/student.txt")

# Convert the timestamp to a readable string format
print("Modification time (ctime):", time.ctime(mod_time))

# Convert the timestamp to a datetime object for easier manipulation
mod_datetime = datetime.fromtimestamp(mod_time)
print("Modification time (datetime):", mod_datetime)

# Calculate how long ago the file was modified
time_delta = datetime.now() - mod_datetime
print(f"It has been {time_delta} since the file was modified.")
print(f"Or {time_delta.total_seconds()} seconds.")
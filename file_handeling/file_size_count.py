"""
Count the Size of Text Files in a Directory

Description:

This Python program calculates the total size in bytes of all .txt files
inside the deps directory. It ignores other file types and returns the total 
byte count.

"""

import os
from os import path

def file_info():
    total_bytes = 0

    for filename in os.listdir("deps"):
        if filename.endswith(".txt"):
            file_path = os.path.join("deps", filename)
            total_bytes += os.path.getsize(file_path)

    return total_bytes
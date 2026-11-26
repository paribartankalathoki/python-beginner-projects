import os
from os import path
import shutil  # Module for high-level file operations like copying
from zipfile import ZipFile  # Module to create and read ZIP archives

# Check if a file exists before working with it
if path.exists("file_handeling/student.txt"):

    # Get the absolute real path of the file
    source = path.realpath("file_handeling/student.txt")

    # Define a backup file name by appending .bak
    destination = source + ".bak"

    # Copy the original file to the backup file
    shutil.copy(source, destination)

    # Rename the original file
    os.rename("file_handeling/student.txt", "studentfile_new.txt")

    # Get the directory path of the source file
    root_dir, _ = path.split(source)

    # Create a ZIP archive of the directory containing the file
    shutil.make_archive("archive", 'zip', root_dir)

    # Create a ZIP file and add specific files to it
    with ZipFile("testzip.zip", 'w') as newzip:
        newzip.write("studentfile_new.txt")  # Add renamed file
        newzip.write("file_handeling/student.txt.bak")  # Add backup file

else:
    print("The file 'file_handeling/student.txt' does not exist. Please create it first.")
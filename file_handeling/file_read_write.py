
# Python File Handling - Read and Write

# File handling allows us to create, read, write and update files.
# Common modes: "r" = Read, "w" = Write, "a" = Append, "x" = Create.


# 1. Write Mode (w+)

# Open a file in write and read mode
# NOTE: "w+" creates a file if it doesn't exist.
# If the file already exists, its previous content will be erased.

file = open("file_handeling/student.txt", "w+")

# Write content into the file
file.write("My name is Ram.\n")
file.write("I am learning Python.")

# Always close the file after working with it
file.close()

# NOTE: write() adds text to a file.


# 2. Read Mode (r)

# Open the file in read mode
# NOTE: "r" only allows reading and requires the file to exist.

file = open("file_handeling/student.txt", "r")

# Read the entire content
content = file.read()

# Print the content
print(content)

# Close the file
file.close()

# NOTE:
# read() reads the entire remaining content.
# readline() reads one line at a time.
# readlines() returns all lines as a list.


# 3. Append Mode (a)

# Open the file in append mode
# NOTE: "a" adds new content without deleting existing content.

file = open("file_handeling/student.txt", "a")

# Add new content at the end of the file
file.write("\nI love programming.")

file.close()

# NOTE:
# Append mode is useful when adding new information.
# Unlike "w", it preserves the existing content.


# 4. Using with open() - Recommended Method

# Open and automatically close the file
# NOTE: Python automatically closes the file after the block ends.

with open("file_handeling/student.txt", "r") as file:

    content = file.read()

    print(content)

# NOTE:
# with open() is considered best practice.
# We don't need to manually call close().
# It also closes the file if an error occurs inside the block.


# Student Marksheet Generator

# Design constants
WIDTH = 66

BORDER = "+" + "-" * (WIDTH - 2) + "+"
LINE = "|" + "-" * (WIDTH - 2) + "|"
SPACE = "|" + " " * (WIDTH - 2) + "|"

# Subject table column widths
COL1 = 6
COL2 = 18
COL3 = 11
COL4 = 16
COL5 = 11

TABLE_LINE = (
    "+" + "-" * COL1
    + "+" + "-" * COL2
    + "+" + "-" * COL3
    + "+" + "-" * COL4
    + "+" + "-" * COL5 + "+"
)


# Keeps every normal marksheet row at the same width
def print_line(text=""):
    print("|" + text.ljust(WIDTH - 2)[:WIDTH - 2] + "|")


# Welcome screen
print("\n")

print(BORDER)
print(SPACE)
print_line("ABC INTERNATIONAL SCHOOL".center(WIDTH - 2))
print_line("STUDENT MARKSHEET SYSTEM".center(WIDTH - 2))
print_line("Academic Result Management".center(WIDTH - 2))
print(SPACE)
print(BORDER)

print(SPACE)
print_line("Welcome to Student Marksheet Generator!".center(WIDTH - 2))
print(SPACE)

print_line("MARKSHEET FEATURES:")
print_line("[1] Student Personal Information")
print_line("[2] Subject-wise Marks Entry")
print_line("[3] Automatic Grade Calculation")
print_line("[4] Total Marks and Percentage")
print_line("[5] Overall Result (PASS / FAIL)")
print_line("[6] Teacher Remarks and Signature")

print(SPACE)
print(BORDER)

print(SPACE)
print_line("INSTRUCTIONS:")
print_line("- Enter student details when requested.")
print_line("- Enter subject names and marks.")
print_line("- The system calculates results automatically.")
print_line("- Your marksheet will be displayed in the console.")

print(SPACE)
print(BORDER)
print(SPACE)

input("|" + "Press ENTER to Generate Marksheet".center(WIDTH - 2) + "|")
print("\n\n")


# Student information
school = "ABC INTERNATIONAL SCHOOL"
year = "2026-2027"

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
class_name = input("Enter Grade/Class: ")
section = input("Enter Section: ")
father = input("Enter Father's Name: ")
dob = input("Enter Date of Birth (yyyy-mm-dd): ")


# Collect subject details in a list
subjects = []

n = int(input("\nEnter Number of Subjects: "))

for i in range(n):
    print("\nSubject", i + 1)

    subject = input("Subject Name: ")
    maximum = int(input("Maximum Marks: "))
    obtained = int(input("Obtained Marks: "))

    subjects.append([subject, maximum, obtained])


# Print marksheet header
print("\n")
print(BORDER)

print_line(school.center(WIDTH - 2))
print_line("STUDENT ACADEMIC MARKSHEET".center(WIDTH - 2))
print_line(("Academic Year: " + year).center(WIDTH - 2))

print(BORDER)

print_line("Student Name  : " + name)
print_line(
    "Roll Number   : " + roll
    + "       Class : " + class_name
    + "    Section: " + section
)
print_line("Father's Name : " + father)
print_line("Date of Birth : " + dob)

print(BORDER)


# Subject table heading
print(
    "|"
    + "S.No".center(COL1) + "|"
    + "Subject".ljust(COL2) + "|"
    + "Max Marks".center(COL3) + "|"
    + "Obtained Marks".center(COL4) + "|"
    + "Grade".center(COL5) + "|"
)

print(TABLE_LINE)


# Calculate subject grades and total marks
total_max = 0
total_obtained = 0

for i, subject in enumerate(subjects, 1):

    subject_name = subject[0]
    maximum = subject[1]
    obtained = subject[2]

    percentage = obtained / maximum * 100 if maximum > 0 else 0

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    total_max += maximum
    total_obtained += obtained

    print(
        "|"
        + str(i).center(COL1) + "|"
        + subject_name.ljust(COL2)[:COL2] + "|"
        + str(maximum).center(COL3) + "|"
        + str(obtained).center(COL4) + "|"
        + grade.center(COL5) + "|"
    )

print(TABLE_LINE)


# Calculate overall percentage and grade
percentage = (total_obtained / total_max * 100) if total_max else 0

if percentage >= 90:
    overall_grade = "A+"
elif percentage >= 80:
    overall_grade = "A"
elif percentage >= 70:
    overall_grade = "B+"
elif percentage >= 60:
    overall_grade = "B"
elif percentage >= 50:
    overall_grade = "C"
else:
    overall_grade = "F"


# A student must score at least 33% in every subject to pass
result = "PASS"

for subject in subjects:
    if subject[1] <= 0 or subject[2] < subject[1] * 0.33:
        result = "FAIL"


# Print result summary
print_line("Total Maximum Marks : " + str(total_max))
print_line("Total Obtained Marks: " + str(total_obtained))
print_line("Percentage          : " + f"{percentage:.2f}%")
print_line("Overall Grade       : " + overall_grade)
print_line("Result              : " + result)

print(BORDER)


# Calculate teacher remarks
if percentage >= 90:
    remarks = "Outstanding Performance!"
elif percentage >= 80:
    remarks = "Excellent Performance!"
elif percentage >= 70:
    remarks = "Very Good Performance!"
elif percentage >= 60:
    remarks = "Good Performance!"
else:
    remarks = "Needs Improvement!"

print_line("Class Teacher Remarks: " + remarks)

print(SPACE)
print(SPACE)

print_line("Teacher Signature: __________   Principal: __________")

print(SPACE)
print_line("Date: " + dob)

print(BORDER)

print("\nMarksheet Generated Successfully!")

from datetime import date
from datetime import datetime

## DATE OBJECTS

# Get today's date and time
today = datetime.today()
print("Today's date is ", today)

# Print individual date components
print("Year, Month and Day:", today.year, today.month, today.day)

# Retrieve today's weekday (0=Monday, 6=Sunday)
print("Week day is:", today.weekday())


## DATETIME OBJECTS

# Get today's date and time
print("Today's date and time is:", datetime.now())

# Get the current time
print("Current time is:", datetime.now().time())

# Example of Getter, Setter and Deleter using @property

class GetterSetterExample:

    # Constructor: Runs automatically when an object is created
    def __init__(self, name):

        # Assign the given name using the setter method
        self.name = name

    # GETTER
    # @property allows us to access a method like a normal attribute
    # For example: example.name instead of example.name()
    @property
    def name(self):

        # Return the value stored in the private attribute _name
        return self._name

    # SETTER
    # Runs automatically whenever we assign a new value to example.name
    # For example: example.name = "John"
    @name.setter
    def name(self, value):

        # Store the given value in the _name attribute
        self._name = value

    # DELETER
    # Runs automatically when we delete example.name
    # For example: del example.name
    @name.deleter
    def name(self):

        # Delete the internal _name attribute
        del self._name


# Create an object and pass "ram" as the initial name
example = GetterSetterExample("ram")


# GETTER is called automatically when we access example.name
print(example.name)  # Output: ram


# DELETER is called automatically and removes the _name attribute
del example.name


# Try to access the name after deleting it
try:

    # This will raise an AttributeError because _name no longer exists
    print(example.name)

except AttributeError as e:

    # Handle the error and display its message
    print("Error:", e)

    # Output: Error: 'GetterSetterExample' object has no attribute '_name'


# This will also raise an AttributeError because the name was already deleted
print(example.name)

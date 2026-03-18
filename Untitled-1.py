# OOP Concepts in Python: Objects, Classes, Constructors, and Destructors

# Define a class
class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Constructor called: {self.name} object created")

    # Method
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Destructor
    def __del__(self):
        print(f"Destructor called: {self.name} object destroyed")


# Create objects
student1 = Student("John", 21)
student2 = Student("Alice", 22)

# Access methods
student1.display()
student2.display()

# Delete an object
del student1

print("Program End")


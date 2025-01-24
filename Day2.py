#Q: Create a List, tuple and Dictionary with 5 elements in it and how to access few elements based on the index. Try  with different examples 


# Creating a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Accessing elements by index
print(fruits[0])  # First element: apple
print(fruits[3])  # Fourth element: date
print(fruits[-1]) # Last element: elderberry

# Creating a tuple
colors = ("red", "blue", "green", "yellow", "purple")

# Accessing elements by index
print(colors[1])  # Second element: blue
print(colors[-2]) # Second-to-last element: yellow


# Creating a dictionary
student_marks = {
    "John": 85,
    "Emma": 92,
    "Liam": 78,
    "Sophia": 88,
    "Olivia": 91
}

# Accessing elements by key
print(student_marks["Emma"])  # Value for key 'Emma': 92
print(student_marks.get("Liam"))  # Value for key 'Liam': 78

print(fruits[1:4])  # Slicing elements from index 1 to 3: ['banana', 'cherry', 'date']
print(fruits[:3])   # First three elements: ['apple', 'banana', 'cherry']

print(colors[2:])   # From index 2 to end: ('green', 'yellow', 'purple')
print(colors[:2])   # First two elements: ('red', 'blue')

print(student_marks.keys())    # All keys: dict_keys(['John', 'Emma', 'Liam', 'Sophia', 'Olivia'])
print(student_marks.values())  # All values: dict_values([85, 92, 78, 88, 91])
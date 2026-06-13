# ============================================
# DAY 1 — Python things you need for ML
# You know basics. These are the GAPS to fill.
# ============================================

# ---- 1. LIST COMPREHENSIONS ----
# Old way you already know:
squares_old = []
for i in range(1, 6):
    squares_old.append(i ** 2)

# Professional way (list comprehension):
squares_new = [i ** 2 for i in range(1, 6)]

print("Old way:", squares_old)
print("New way:", squares_new)
# Both give same result. ML code uses new way everywhere.

# With condition:
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print("Even squares:", even_squares)


# ---- 2. LAMBDA FUNCTIONS ----
# A function without a name. Used heavily in pandas later.

# Normal function:
def double_normal(x):
    return x * 2

# Lambda version (same thing, one line):
double_lambda = lambda x: x * 2

print(double_normal(5))   # 10
print(double_lambda(5))   # 10

# Lambda with two inputs:
add = lambda x, y: x + y
print(add(3, 4))   # 7


# ---- 3. MAP AND FILTER ----
# map() applies a function to every item in a list
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)   # [2, 4, 6, 8, 10]

# filter() keeps only items where condition is True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)   # [2, 4]


# ---- 4. EXCEPTION HANDLING ----
# Prevents your program from crashing on bad input
# Critical when reading files or user data in projects

try:
    result = 10 / 0          # This will cause an error
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    number = int("hello")    # Can't convert text to int
except ValueError as e:
    print(f"Error caught: {e}")

# Always use try/except when reading files or APIs in projects


# ---- 5. FILE HANDLING ----
# You'll read/write data files in every ML project

# Writing a file:
with open("test_file.txt", "w") as f:
    f.write("Name,Age,Score\n")
    f.write("Alice,21,85\n")
    f.write("Bob,22,91\n")
    f.write("Charlie,20,78\n")

print("File written!")

# Reading it back:
with open("test_file.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line (better for large files):
with open("test_file.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes \n at end


# ---- 6. DICTIONARIES - ADVANCED ----
# You know basic dicts. This is how ML code uses them.

student = {
    "name": "Sai",
    "scores": [85, 90, 78, 92],
    "branch": "AIDS"
}

# Get average score using list comprehension:
avg = sum(student["scores"]) / len(student["scores"])
print(f"{student['name']}'s average: {avg:.2f}")

# Dictionary comprehension (like list comprehension):
scores = {"Alice": 85, "Bob": 91, "Charlie": 78}
passed = {name: score for name, score in scores.items() if score >= 80}
print("Passed students:", passed)


# ---- 7. F-STRINGS (professional way to print) ----
name = "Sai Teja"
branch = "AIDS"
year = 3
cgpa = 8.75

# Old way (ugly):
print("Name: " + name + ", Branch: " + branch)

# Professional way (f-string):
print(f"Name: {name}, Branch: {branch}, Year: {year}, CGPA: {cgpa:.2f}")
# :.2f means 2 decimal places

# ============================================
# TASK FOR YOU — write your own code below:
# 1. Create a list of 10 numbers using range
# 2. Use list comprehension to get cubes of odd numbers only
# 3. Use filter+lambda to keep only numbers > 50
# 4. Print results with f-strings
# ============================================
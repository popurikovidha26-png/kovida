
# Tuple Operations

# 1. Tuple Concatenation
t1 = (10, 20, 30)
t2 = (40, 50, 60)

t3 = t1 + t2
print("Concatenated Tuple:", t3)

# 2. Tuple Slicing
t = (10, 20, 30, 40, 50, 60)

print("Sliced Tuple:", t[1:4])

# 3. Tuple Unpacking
student = ("Kovida", 20, "CSE")

name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)

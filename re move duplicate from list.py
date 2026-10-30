# Creating a list
my_list = [10, 20, 30, 20, 40, 10, 50]

print("Original List:", my_list)

# Removing duplicate elements
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

# Displaying the result
print("List after removing duplicates:", new_list)

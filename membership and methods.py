
# Create a set
my_set = {10, 20, 30, 40, 50}

# Display the set
print("Original Set:", my_set)

# Membership testing
print("Is 20 present?", 20 in my_set)
print("Is 60 present?", 60 in my_set)

# Add an element
my_set.add(60)
print("After adding 60:", my_set)

# Remove an element
my_set.remove(30)
print("After removing 30:", my_set)

# Discard an element
my_set.discard(40)
print("After discarding 40:", my_set)

# Discard a non-existing element
my_set.discard(100)
print("After discarding 100:", my_set)

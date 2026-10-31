n = int(input("Enter how many numbers: "))

largest = int(input("Enter a number: "))

for i in range(n - 1):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num

print("Largest number =", largest)

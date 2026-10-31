n = int(input("Enter how many numbers: "))
total = 0

for i in range(n):
    num = int(input("Enter a number: "))
    total += num

average = total / n

print("Sum =", total)
print("Average =", average)

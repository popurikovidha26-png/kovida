n = int(input("Enter a number (1-100): "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if n > 1 and count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

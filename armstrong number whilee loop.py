n = int(input("Enter a 3-digit number: "))
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

if total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

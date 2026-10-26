n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if n == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

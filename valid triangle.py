

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

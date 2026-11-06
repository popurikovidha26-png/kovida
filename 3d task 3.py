def calculate(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

a = int(input("Enter first subject marks: "))
b = int(input("Enter second subject marks: "))
c = int(input("Enter third subject marks: "))

total, average = calculate(a, b, c)

print("Total Marks:", total)
print("Average Marks:", average)

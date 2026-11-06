def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

p = float(input("Enter principal: "))
t = float(input("Enter time: "))

# Calling with default rate
print("Simple Interest (Default Rate):", simple_interest(p, t))

# Calling with explicit rate
r = float(input("Enter rate: "))
print("Simple Interest (Explicit Rate):", simple_interest(p, t, r))

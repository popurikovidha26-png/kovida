s = input("Enter a string: ")

for ch in set(s):
    print(ch, ":", s.count(ch))

num = int(input("Enter a number: "))
orig_num = num
work = num
rev=0
while work> 0:
    digit = work % 10
    rev = rev*10 + digit
    work = work // 10
if rev == orig_num:
    print(f"{orig_num} is an palindrome ")
else:
    print(f"{orig_num} is not an palindrome")
   

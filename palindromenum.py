n = int(input("Enter number: "))

temp = n
rev = 0

while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp //= 10

if rev == n:
    print("Palindrome Number")
else:
    print("Not a Palindrome")
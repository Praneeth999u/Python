n = int(input("Enter number: "))

sum_d = 0
prod = 1

temp = n
while temp > 0:
    d = temp % 10
    sum_d += d
    prod *= d
    temp //= 10

if sum_d == prod:
    print("Spy Number")
else:
    print("Not a Spy Number")
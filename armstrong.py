n = int(input("Enter number: "))

power = len(str(n))
sum = 0

temp = n
while temp > 0:
    d = temp % 10
    sum += d ** power
    temp //= 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
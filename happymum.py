n = int(input("Enter number: "))

while n != 1 and n != 4:
    sum = 0
    while n > 0:
        d = n % 10
        sum += d * d
        n //= 10
    n = sum

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
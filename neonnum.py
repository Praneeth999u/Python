n = int(input("Enter number: "))

sq = n * n
sum = 0

while sq > 0:
    d = sq % 10
    sum += d
    sq //= 10

if sum == n:
    print("Neon Number")
else:
    print("Not a Neon Number")
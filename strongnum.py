n = int(input("Enter number: "))

sum = 0
temp = n

while temp > 0:
    d = temp % 10
    
    fact = 1
    for i in range(1, d + 1):
        fact *= i
        
    sum += fact
    temp //= 10

if sum == n:
    print("Strong Number")
else:
    print("Not a Strong Number")
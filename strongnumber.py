def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n -1) * n 
         

T = int(input())   #reading multiple test cases

for _ in range(T):
    n = int(input())
    sum = 0
    temp = n
    while n != 0 :
        rem = n % 10
        n = n // 10
        sum = sum + fact(rem)
    if sum == temp:
        print("Strong")

    else:
        print("Not Strong")

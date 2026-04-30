n = input("Enter number: ")

sum = 0

for i in range(len(n)):
    sum += int(n[i]) ** (i + 1)

if sum == int(n):
    print("Disarium Number")
else:
    print("Not a Disarium Number")
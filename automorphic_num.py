n = int(input("Enter number: "))

sq = n * n

if str(sq).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
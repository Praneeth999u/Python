s = input()
n = len(s)
rev = ""
for i in range (n-1,-1,-1):
    rev = rev + s[i]
print(rev)


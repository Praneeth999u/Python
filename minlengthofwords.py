s = input()
m = s.split()
min = len(m[0])
for i in range(1, len(m)) :
    if( len(m[i]) < min ):
        min = len(m[i])

print(min)


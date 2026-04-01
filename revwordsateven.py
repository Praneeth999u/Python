def reverse(s):
    rev = ""
    for i in range(len(s)- 1, -1 , -1):
        rev = rev + s[i]
    return rev

s = input()
m = s.split()
rev2 = ""
for j in  range (0,len(m)):
    if j % 2 == 0 :
            rev2 = rev2 + reverse(m[j])
    else:
        rev2 = rev2 + m[j]
    rev2 = rev2 + " "
print(rev2) 


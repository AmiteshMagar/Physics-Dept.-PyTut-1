j1 = int(input("enter j1"))
j2 = int(input("enter j2"))
ls = []
for i in range(abs(j1-j2),abs(j1 +j2)+1,1):
    ls.append(i)
print(ls)

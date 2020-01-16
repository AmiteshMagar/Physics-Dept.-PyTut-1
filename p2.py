r1 = int(input("Enter the number of rows in first matrix"))
c1=int(input("Enter the number of columns in first matrix"))
a = [[ 0 for i in range(c1)] for j in range(r1)]
print("Enter the elements of the first matrix")
for i in range(r1):
    for j in range(c1):
        a[i][j] = int(input())
r1 = int(input("Enter the number of rows in second matrix"))
c1 = int(input("enter the number of columns in the second matrix"))
b = [[0 for  i in range(c1)] for  j in range(r1)]
print("Enter the elements of the second matrix")
for  i in range(r1):
    for  j in range(c1):
        b[i][j] = int(input())
rowA = len(a)
colA = len(a[0])
rowB = len(b)
colB = len(b[0])
c = [[0 for i in range(colB)] for j in range(rowB)]

def add(mat1, mat2):
    if rowA==rowB and colA==colB:
        print("addition is possible")
        for i in range(rowA):
            for j in range(colB):
                c[i][j] = mat1[i][j] + mat2[i][j]
        return c
    else:
        print("Addition is not possible")

def mul(mat1,mat2):
    c = [[0 for i in range(colB)] for j in range(rowA)]
    if colA==rowB:
        print("multiplication is possible")
        for i in range(colB):
            for j in range(rowA):
                for k in range(colA):
                    c[i][j] = c[i][j] + (mat1[i][k]*mat2[k][j])
        return c
    else:
        print("Multiplication is not possible")

print(add(a,b))
print(mul(a,b))


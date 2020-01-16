x1 = int(input("Input x1"))
fx1 = int(input("Input f(x1)"))
x2 = int(input("Input x2"))
fx2 = int(input("Input f(x2)"))

m = (fx2 - fx1)/(x2 - x1)
x = int(input("Enter x"))
y = fx1 + m*(x-x1)
print(y)

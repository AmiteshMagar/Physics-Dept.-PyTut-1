import math
def fibre(n1,n2,D,L):
    Na = math.sqrt((n1**2)-(n2**2))
    Nm = (0.5 * math.pi * D * Na)/L
    return Nm

n1 = int(input())
n2 = int(input())
D = float(input())
L = float(input())
print(fibre(n1,n2,D,L))

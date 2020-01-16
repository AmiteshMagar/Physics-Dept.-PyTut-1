import math
def oper(n,ls):
    mx = max(ls)
    mn = min(ls)
    su = 0
    pro = 1
    powerSum = 1
    for i in ls:
        su = su + ls
        pro = pro * ls
        powerSum = powerSum + i**2
    powerAvg = powerSum/n
    avg = su/n
    variance = powerAvg - (avg**2)
    stDev = math.sqrt(variance)
    

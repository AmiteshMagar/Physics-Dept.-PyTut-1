def power(vs,rs,Rl):
    res = (rs + Rl)**2
    P = (vs**2)*Rl/res
    return P

vs = 12
rs = 2.5
for Rl in range(1,13):
    print(power(vs,rs,Rl))
    

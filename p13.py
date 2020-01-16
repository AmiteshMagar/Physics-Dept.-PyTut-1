wt = float(input())
wt = wt//(0.1)
ht  = float(input())

BMI = wt/(ht**2)

if BMI>=20 and BMI<=24.9:
    grade = 0
    status = "desirable"
elif BMI>=25 and BMI<=29.9:
    grade = 1
    status = "overweight"
elif BMI>=30 and BMI<=40:
    grade = 2
    status = "overweight"
elif BMI>40:
    grade = 3
    status = "morbidly obese"
    

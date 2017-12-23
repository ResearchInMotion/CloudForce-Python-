import math
a=int(input("Please enter the number "))
b=int(input("Please enter the number "))
c=int(input("Please enter the number "))
d=int(input("Please enter the number "))

cubeofa=math.pow(a,3)
cubeofb=math.pow(b,3)
cubeofc=math.pow(c,3)
cubeofd=math.pow(d,3)

sum=cubeofa+cubeofb+cubeofc

if(sum==cubeofd):
    print("the equation is satisfied")
else:
    print("the equation is not satisfied")
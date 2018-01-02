import math
Number=int(input("please enter the number "))
Radius=int(input("please enter the radius "))
if(Number==1):
    area=3.14*math.pow(Radius,2)
    print("The area is",area)
else:
    circumfrence=2*3.14*Radius
    print("The Circumfrence is ",circumfrence)

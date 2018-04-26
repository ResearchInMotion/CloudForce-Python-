year=int(input("Please enter the year : "))



flag = False;


if(year%400==0):
    flag=True
elif(year%100==0):
    flag=False
elif(year%4==0):
    flag=True
else:
    flag=False



if(flag):
    print("Leap year ")
else:
    print("Not a leap year ")
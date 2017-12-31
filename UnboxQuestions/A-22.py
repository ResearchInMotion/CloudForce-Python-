import math
Number=int(input("Please enter a number "))
if(Number%2==0):
    Number=math.pow(Number,2)
    print("The number is even, so we are printing the Power ",Number)
else:
    Number=math.pow(Number,3)
    print("The Number is odd , so we are taking",Number)

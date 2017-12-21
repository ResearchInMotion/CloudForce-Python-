from MathematicalFunctions import areaofsquare,rectangle,parllelogram,trapezoid,circle

number1=int(input("Please enter the number1 "))
number2=int(input("Please enter the number2 "))
number3=int(input("Please enter the number3 "))

print("The area of square is ",areaofsquare(number1))
print("The area of rectangle is ",rectangle(number1,number2))
print("The area of parelellogram is ",parllelogram(number2,number1))
print("The area of trapezoid is ",trapezoid(number1,number2,number3))
print("The area of circle is ",circle(number2))


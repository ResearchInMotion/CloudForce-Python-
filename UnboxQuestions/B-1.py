Subject1=int(input("Marks "))

Subject2=int(input("Marks "))

Subject3=int(input("Marks "))

Subject4=int(input("Marks "))

Subject5=int(input("Marks "))
print("Marks in Subject1",Subject1)
print("Marks in Subject2",Subject2)
print("Marks in Subject3",Subject3)
print("Marks in Subject4",Subject4)
print("Marks in Subject5",Subject5)


Sum_percentage=int((Subject1+Subject2+Subject3+Subject4+Subject5)/5)
print("Sum of numbers are",Sum_percentage)


if(Sum_percentage>=60):
    print("First division")
elif(Sum_percentage>=50 and Sum_percentage<59):
    print("Second division")
elif(Sum_percentage>=40 and Sum_percentage<49):
    print("Third division")
elif(Sum_percentage<40):
    print("fail")
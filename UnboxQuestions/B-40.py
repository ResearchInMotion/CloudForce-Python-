
num1=int(input("Please enter the number "))
num2=int(input("Please enter the number "))



i=num1
sum=0
while i<num2:
    if (i%2==0 and i%3==0 and i%5!=0):
        sum=sum+i
    i=i+1
print("The sum of range numbers are ",sum)



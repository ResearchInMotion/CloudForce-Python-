number=int(input("please enter Number "))
number2=int(input("please enter Number2 "))
Choice=input("please enter your choice ")

if(Choice=='+'):
    Addition=number+number2
    print(Addition)
elif(Choice=='-'):
    Subtract=number-number2
    print(Subtract)
elif(Choice=='*'):
    Multiply=number*number2
    print(Multiply)
elif(Choice=='/'):
    Divide=number/number2
    print(Divide)
elif(Choice=='%'):
    Reminder=number%number2
    print(Reminder)
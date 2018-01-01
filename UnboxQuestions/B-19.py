x=int(input("please enter your choice "))

if(x==1):
    Temperature=int(input("Please enter the value of temperature in celsius "))
    fah=Temperature*9/5+32

    print("The temperature in faherenhiet is ",fah)
elif(x==2):
    Temperature2=int(input("Please enter the value if temperature in faherenhiet "))
    cel=(Temperature2-32)*5/9

    print("the temperature in celsius is ",cel)
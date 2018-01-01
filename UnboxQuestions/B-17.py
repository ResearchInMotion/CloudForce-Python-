subject1=int(input("Please enter the marks for first student "))
subject2=int(input("Please enter the marks for second student "))
subject3=int(input("Please enter the marks for third student "))
subject4=int(input("Please enter the marks for fourth student "))
subject5=int(input("Please enter the marks for fifth student "))

sumofnumbers=(subject1+subject2+subject3+subject4+subject5)/5



if(sumofnumbers>=90):
    print("The Grade is S")
elif(sumofnumbers>76 and sumofnumbers<90):
    print("The Grade is A")
elif (sumofnumbers > 61 and sumofnumbers < 75):
    print("The Grade is B")
elif(sumofnumbers>51 and sumofnumbers<60):
    print("The Grade is C")
elif(sumofnumbers>40 and sumofnumbers<50):
    print("The Grade is D")
elif(sumofnumbers<40):
    print("you are Fail")

Salary = int(input("Please enter the salary : "))

if((Salary>5000) & (Salary<10000)):
    hra=Salary*0.10
    da=Salary*0.05


elif((Salary>10001) & (Salary<15000)):
    hra = Salary * 0.15
    da = Salary * 0.08

print("The HRA is " ,hra )
print("The DA is ",da)
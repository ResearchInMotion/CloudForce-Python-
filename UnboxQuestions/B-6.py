year=int(input("please enter the year "))
diff=(year%100)
leap_yr=(year%100)/4
total_days=(diff*365)*leap_yr
days_of_weak=r=total_days%7
if(days_of_weak==0):
    print("Monday")
elif(days_of_weak==1):
    print("tuesday")
elif(days_of_weak==2):
    print("Wednesday")
elif(days_of_weak==3):
    print("Thursday")
elif(days_of_weak==4):
    print("Friday")
elif(days_of_weak==5):
    print("saturday")
elif(days_of_weak==6):
    print("Sunday")
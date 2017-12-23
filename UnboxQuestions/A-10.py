Days=int(input("Please enter the number of days"))
Year=Days/365
Days=Days%365
Weeks=Days/7
Days=Days%7
Day=Days
print("No of years : ",Year)
print("No of weeks : ",Weeks)
print("No of days : ",Day)
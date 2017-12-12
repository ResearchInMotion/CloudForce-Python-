numbers=int(input("please insert the stack value of numbers  "))
total_sum=0

for n in range(numbers):
    numbers=int(input("enter the numbers  "))
    total_sum +=numbers


average=total_sum/numbers
print("avergae is " ,average)
print("sum is",total_sum)
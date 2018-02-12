arr=[]
limit=int(input("Please enter your number "))
for val in range(0,limit):
    arr.append(int(input("Please enter the next number ")))
sortedArray=sorted(arr)
print(sortedArray)

arr.append(int(input("Please enter the next number ")))
sortedArray=sorted(arr)
print(sortedArray)
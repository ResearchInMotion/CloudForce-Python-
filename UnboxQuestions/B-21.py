arr=[]

size=int(input("Please enter the size of array "))

for va in range(0,size):
    arr.append(int(input("Please enter the elements : ")))
print(arr)


print("Sorted numbers are : ")

print(sorted(arr))


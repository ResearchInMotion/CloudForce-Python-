arr=[]
Limit=int(input("Please enter the limit of the array : "))

for value in range(0,Limit):
    arr.append(int(input("Please enter the number , you want to add : ")))




arr2=[]
Limit2=int(input("Please enter the limit of the array 2 : "))

for value2 in range(0,Limit2):
    arr2.append(int(input("Please enter the digits , you want to enter : ")))

print(arr)
print(arr2)


arr_after_5=arr[5:]


arr_after_5.append(arr2[5:])
print(arr_after_5)


val=4
arr1=[]
arr2=[]
arr3=[]

size=int(input("Please enter the size for the first list : "))

for i in range(0,size):
    arr1.append(int(input("Please enter the values in arr : ")))

print(arr1)


size2=int(input("Please enter the size for the Second list : "))

for i2 in range(0,size2):
    arr2.append(int(input("Please enter the values in arr : ")))

print(arr2)

size3=int(input("Please enter the size for the Third list : "))

for i3 in range(0,size3):
    arr3.append(int(input("Please enter the values in arr : ")))

print(arr3)

the_list=[]

the_list.append(arr1)
the_list.append(arr2)
the_list.append(arr3)

print(the_list)
print(the_list[1][0])



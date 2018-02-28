Arr=[]
Arr2=[]

print("********Please ensure that the arrays you are inserting are of same size *******")
size=int(input("Please enter the size of the first array : "))

for val in range(0,size):
    Arr.append(int(input("Please enter the element : ")))

print(Arr)

for val2 in range(0,size):
    Arr2.append(int(input("Please enter the element : ")))

print(Arr2)


Arr3=[]

Arr3=Arr+Arr2
Arr4=sorted(Arr3)

print(Arr3)
print(Arr4)

Arr=[]

Size=int(input("Please enter the size of the array : "))

for val in range(0,Size):
    Arr.append(int(input("Please enter the value : ")))

print(Arr)


print("The size of your array is : ",len(Arr))

middle_values=len(Arr)/2

if(int(middle_values)%2==0 ):
    middle_values += 1
else:
    middle_values+=0.5

print("So probably the middle value of your array is " , middle_values)


Arr.pop(int(middle_values))

print(Arr)




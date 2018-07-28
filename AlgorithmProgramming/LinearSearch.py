def LinearSearch(arr,number):
    for values in range(len(arr)):
        if(number==arr[values]):
            return values


    return -1




arr=[]

limit = int(input("Please enter the number : "))


for values in range(0,limit):

    arr.append(int(input("Please enter the elements : ")))

print(arr)



number = int(input("Please enter the number : "))

result = LinearSearch(arr,number)

if(result!=-1):
    print("The values is present ")
else:
    print("The value is not present ")



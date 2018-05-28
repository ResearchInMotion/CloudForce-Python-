def BinarySearch(arr,low,high,number):

    if(high>=low):

        mid = int(low+(high-low)/2)

        if(arr[mid]==number):
            return mid

        elif(arr[mid]>number):
            return BinarySearch(arr,low,mid-1,number)
        else:
            return BinarySearch(arr,mid+1,high,number)

    else:
        return -1



arr=[]

limit = int(input("Please enter the limit : "))

for values in range(0,limit):

    arr.append(int(input("Please enter the number : ")))

print(arr)


number = int(input("Please enter the number to search : "))

result = BinarySearch(arr,0,len(arr)-1,number)

if(result!=-1):
    print("Element is present at index %d" % result)
else:
    print("Sorry not found")
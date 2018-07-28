def partition(arr,low,high):


    i=(low-1)

    pivot=arr[high]

    for j in range(low,high):

        if(arr[j]<= pivot):

            i+=1

            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)

def quickSort (arr,low,high):

    if(high>low):
        pi = partition(arr,low,high)

        quickSort(arr, low, pi - 1)
        quickSort(arr,pi+1,high)






arr=[]

limit = int(input("Please enter the limit : "))

for values in range(0,limit):

    arr.append(int(input("Please enter the number : ")))

print("The unsorted array is : ",arr)

quickSort(arr,0,len(arr)-1)


print("sorted array is : ")

for val in range(len(arr)):
    print("%d" %arr[val])



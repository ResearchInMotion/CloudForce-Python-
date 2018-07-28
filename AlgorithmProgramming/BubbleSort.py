def BubbleSort(arr):

    for i in range (len(arr)):

        for j in range(0,len(arr)-i-1):

            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]






arr=[]


limit = int(input("Please enter the limit : "))

for values in range(0,limit):
    arr.append(int(input("Please enter the number : ")))


print(arr)

BubbleSort(arr)

print("Sorted array is : ")
for value in range(len(arr)):
    print(arr[value])




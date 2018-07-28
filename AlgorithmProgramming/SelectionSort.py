def selectionSort(arr):


    for i in range(0,len(arr)):

        min_element=i

        for j in range(i+1,len(arr)):

            if(arr[min_element]>arr[j]):
                    min_element=j


            arr[i],arr[min_element]=arr[min_element],arr[i]

    print("The sorted array is : ",arr)



arr=[]

size = int(input("Please enter the size of element :"))

for values in range(0,size):
    arr.append(int(input("Please enter the values : ")))

print("the unsorted array is : ",arr)

selectionSort(arr)


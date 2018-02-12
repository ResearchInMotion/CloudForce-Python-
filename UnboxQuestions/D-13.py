



Arr=[123,65,456,121,567,55]



for val in Arr:
    temp = val
    rev = 0
    add=0



    while(val>0):
        dig=val%10
        rev=rev*10+dig
        val=val//10

    if(temp==rev):

        print("The number which is palindrome : ",temp )







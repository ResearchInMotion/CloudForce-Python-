arr=[]
limit=int(input("Please enter the limit"))
for val in range(0,limit):
    arr.append(int(input("Please enter the next value")))
print(arr)
counteven=0
countodd=0
countnegative=0
countpositive=0
for i in arr:
    if(i%2==0):
        counteven+=1
    elif(i%2==1):
        countodd+=1
    elif(i<0):
        countnegative+=1
    elif(i>0):
        countpositive+=1
    else:
        print("bye")



print(countodd)
print(counteven)
print(countnegative)
print(countpositive)

Arr=[54,65,76,34,23,12,4,5,78,56]

total=sum(Arr)
average=total/10
print(total)
print(average)

for i in Arr:
    if(i>average):
        print(i)

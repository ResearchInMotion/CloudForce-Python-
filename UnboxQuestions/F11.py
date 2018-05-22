def natural(n):
    sum=0
    for values in range(1,n,2):
        sum+=values
        average=sum/n

    print("The sum is : ",sum)
    print("The Average is : ",average)


natural(10)
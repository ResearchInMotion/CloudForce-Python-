def natural(n):
    sum=0
    for values in range(0,n):
        sum+=values
    average = sum/n
    print("The sum is ",sum)
    print("The average is ",average)


natural(4)
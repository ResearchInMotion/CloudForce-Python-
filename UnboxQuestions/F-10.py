def natural(n):
    if n < 0:
        print("Enter a positive number")
    else:
        sum = 0
        # use while loop to iterate un till zero
        while (n > 0):
            sum += n
            n -= 1
        return sum


print("The sum is ",natural(4))

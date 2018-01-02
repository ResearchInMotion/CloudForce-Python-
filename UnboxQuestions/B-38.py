def sumofevenints (n):

    n >= 1

    total = 0

    for num in range (1, n):

        if num % 2 == 0:
            print("The numbers are ",num)


            total += num

    print (total)
    return total



n=int(input("Please enter the n "))
print("The sum of even ints are ",sumofevenints(n))
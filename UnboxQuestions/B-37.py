def sumofoddints (n):

    n >= 1

    total = 0

    for num in range (1, n):

        if num % 2 == 1:
            print("The numbers are ",num)

            total += num

    print (total)
    return total



n=int(input("Please enter the n "))
print("The sum of odd ints are ",sumofoddints(n))
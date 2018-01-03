Number=int(input("Please enter a number "))

if Number > 1:
    # check for factors
    for i in range(2, Number):
        if (Number % i) == 0:
            print(Number, "is not a prime number")
            print(i, "times", Number // i, "is", Number)
            break
    else:
        print(Number, "is a prime number")

else:
    print(Number, "is not a prime number")
import math
Number=int(input("Please enter a number "))
sqrtt=int(math.sqrt(Number))


if sqrtt > 1:
    # check for factors
    for i in range(2, sqrtt):
        if (sqrtt % i) == 0:
            print(sqrtt, "is not a prime number")
            print(i, "times", sqrtt // i, "is", sqrtt)
            break
    else:
        print(sqrtt, "is a prime number")

else:
    print(sqrtt, "is not a prime number")
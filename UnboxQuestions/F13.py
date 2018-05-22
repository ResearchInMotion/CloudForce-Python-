def prime(number):
    isPrime=True
    for values in range(2,10):
        if(number%values==0):
            isPrime=False
        break

    if(isPrime==True):
        print("Is Prime")
    else:
        print("Is not Prime")


prime(43)

arr = [11,13,14,15,16,17,19]

number = 17

isPrime = True


for val in range(2,10):


    if((number%val)==0):
        isPrime=False
        break


if(isPrime):
    print("Is prime")
else:
    print("Is not Prime")
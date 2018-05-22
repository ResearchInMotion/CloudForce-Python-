def factorial(num):
    fact=1;
    for val in range(num,1,-1):
        fact=fact*val
    print("The factorial of ",num,"is ",fact)

factorial(6)
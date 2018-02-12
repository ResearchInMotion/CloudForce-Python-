Prime_arr=[]
size=int(input("Please enter the size of array : "))

for val in range(0,size):
    Prime_arr.append(int(input("Add the element : ")))


for values in Prime_arr:
    if values > 1:
        # check for factors
        for i in range(2, values):
            if (values % i) == 0:
                print(values, "is not a prime number")
                print(i, "times", values // i, "is", values)
                break
        else:
            print(values, "is a prime number")
            su = sum(map(int, str(values)))
            print("The sum of this prime numbers is : ", su)

    else:
        print(values, "is not a prime number")
        print("Please enter the correct values or your mathematics is weak")



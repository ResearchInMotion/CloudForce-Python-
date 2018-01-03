def lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def gcd(a, b):

    if (a == 0 or b == 0):
        False

    if (a == b):
        return a


    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)



num1=int(input("Please enter the number 1 "))
num2=int(input("Please enter the number 2 "))


if (gcd(num1, num2)):
    print('GCD of', num1, 'and', num2, 'is', gcd(num1, num2))
else:
    print('not found')




print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))

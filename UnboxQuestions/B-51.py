def convertToBinary(n):

   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

decimal=int(input("Please enter the positive integer "))


convertToBinary(decimal)
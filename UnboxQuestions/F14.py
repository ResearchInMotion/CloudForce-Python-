def util(number):

    val=len(str(number))
    print(val)

    val2=(sum(int(number) for number in str(number)))
    print("The sum of all numbers : ",val2)

    val3=sum(map(int,str(number)))
    print("The sum of all numbers are : ",val3)

    val4=str(number)
    val5=val4[::-1]
    print("The reverse is : ",val5)





util(34562)
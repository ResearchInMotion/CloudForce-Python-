def number(a):
    a = input('Enter your list: ')
    mylist = [int(x) for x in a.split(',')]
    total = 0
    for number in mylist:
        total += number
        return total


print("the values are ",number(123))

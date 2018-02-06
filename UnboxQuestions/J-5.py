emp = []


emp = [['Roll Number', 'Name', 'Address', "City" , "Country"]]

f = True
while f:
    print("Hey Welcome Dude/Gorgeous <3 <3")
    print("Please Press Y to add up the data , though data is expensive huh !!",end="\n\n")
    print("Please Press N , If you are fed up !!" , end="\n\n")
    print("Please Press F , oh no this word is only to find the data which you have uploaded , dirty mind !! ",end="\n\n")

    ch = input('Hey Whatsup ! What you have decided : ')

    if ch == 'N':
        f = False

    elif ch == 'Y':
        row = []
        rollnumber = int(input('Please enter the roll number '))
        name = input('Please enter the name ')
        Address = input('Please enter the address ')
        City=input("Please enter the city ")
        Country=input("Please enter the country ")

        row.append(rollnumber)
        row.append(name)
        row.append(Address)
        row.append(City)
        row.append(Country)

        emp.append(row)

    elif ch=='F':
        Choice=input("If you want to visualize the content,Please press V : ")
        if(Choice=='V'):
            roll= input("Please enter the roll number of the student : ")
            for i in range(1, len(emp)):
                    if(emp[i][0]==roll):
                        print(emp[i])



    else:
        print('invalid input you idiot, please choose from above options , look I am using "Please" ')





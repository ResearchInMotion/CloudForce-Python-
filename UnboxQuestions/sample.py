emp = []

# emp = [[],[][,[]]
emp = [['id', 'name', 'Gender', "Sal"]]

f = True
while f:

    ch = input('do you want to add datat then press y and exist press n:')

    if ch == 'n':
        f = False

    elif ch == 'y':
        row = []
        i = input('enter id :')
        name = input('enter name :')
        g = input('enter gender :')
        sal = input('enter sal :')

        row.append(i)
        row.append(name)
        row.append(g)
        row.append(sal)

        emp.append(row)

    else:
        print('invalid input, please choice from given option.')

# print(emp)
for r in emp:
    print(r)
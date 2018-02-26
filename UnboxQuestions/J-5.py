class emp:
    def __init__(s):
        s.Roll_number = 0
        s.Name = ''
        s.Address = ''
        s.City=''
        s.Country=''

    def inp(s):
        s.Roll_number = input('Enter the Roll Number of the student : ')
        s.Name = input('Enter the name of the student : ')
        s.Address = input('Enter the Address of the student : ')
        s.City=input('Enter the City of the student :')
        s.Country=input('Enter the Address of the student :')

    def disp(this):
        print(this.Roll_number)
        print(this.Name)
        print(this.Address)
        print(this.City)
        print(this.Country)

    def getRollNumber(s):
        return s.Roll_number


eo = []
s = int(input('enter the strength of the class  '))

for i in range(0, s):
    o = emp()
    o.inp()
    eo.append(o)

sid = input('enter id to search :')
for i in eo:
    if i.getRollNumber() == sid:
        i.disp()
print("Thanks for your time",end="\n\n")
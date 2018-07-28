class daynames:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None


e1 = daynames('Mon')
e2 = daynames('Tues')
e3 = daynames('Wed')

e1.nextval=e2



e3.nextval = e1



thisvalue = e3

while thisvalue:
    print(thisvalue.dataval)
    thisvalue=thisvalue.nextval
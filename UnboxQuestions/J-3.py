class taxpayer:

    def input(self):
        self.pan=int(input("Please enter the pan number "))
        self.name=input("Please enter you name ")
        self.income=int(input("Please enter the income "))
    def caltax(s):
        s.value=""
        if(s.income<=100000):
            s.value="Enjoy your income is so less"
            return (s.value)
        elif(s.income==1000001 and 200000 ):
            s.value=0.10*s.income
            return (s.value)
        elif (s.income == 200001 and 500000):
            s.value = 0.15 * s.income
            return (s.value)
        elif (s.income>500000):
            s.value = 0.20 * s.income
            return (s.value)

    def disp(city):
        print("The pan number is ",city.pan)
        print("The name is ",city.name)
        print("The income is ",city.income)
        print("The Tax is ",city.value)


ob=taxpayer()
ob.input()
ob.caltax()
ob.disp()
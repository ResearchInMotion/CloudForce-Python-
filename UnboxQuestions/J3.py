from re import search


class Emp:
    def input(self):


        self.Ecode=int(input("Please enter the Ecode : "))
        self.EName = input("Please enter the Ecode : ")
        self.Income = int(input("Please enter the Ecode : "))
        print(self)

    def calculate(self2):
        print(self2)


        if(self2.Income<=1000):
            self2.tax=self2.Income*0
        elif(self2.Income>1001 and self2.Income<2001):
            self2.tax=self2.Income*0.10
        elif (self2.Income > 2001 and self2.Income < 5001):
            self2.tax = self2.Income * 0.15






    def display(self3):
        print(self3)
        print("The Emplpyoyee code is : ",self3.Ecode)
        print("The Name is : ",self3.EName)
        print("The Basic Salary is : ",self3.Income)
        print("The Tax is : ",self3.tax)

obj=Emp()
obj.input()
obj.calculate()
obj.display()






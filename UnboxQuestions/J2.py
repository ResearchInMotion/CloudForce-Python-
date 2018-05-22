class Emp:
    def input(self):


        self.Ecode=int(input("Please enter the Ecode : "))
        self.EName = input("Please enter the Ecode : ")
        self.BasicSalary = int(input("Please enter the Ecode : "))
        print(self)

    def calculate(self2):
        print(self2)

        self2.HRA = 0.40 * self2.BasicSalary
        self2.DA = 0.20 * self2.BasicSalary
        self2.TA = 0.10 * self2.BasicSalary

        self2.GS=self2.BasicSalary+self2.HRA+self2.DA+self2.TA;

    def display(self3):
        print(self3)
        print("The Emplpyoyee code is : ",self3.Ecode)
        print("The Name is : ",self3.EName)
        print("The Basic Salary is : ",self3.BasicSalary)
        print("The HRA is : ",self3.HRA)
        print("The DA is : ",self3.DA)

obj=Emp()
obj.input()
obj.calculate()
obj.display()






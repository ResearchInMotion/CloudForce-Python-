class Student:
    def input(self):
        self.roll_no=int(input("Please enter the number : "))
        self.name=input("Please enter the name : ")
        self.marks1=int(input("Please enter the marks : "))
        self.marks2 = int(input("Please enter the marks : "))
        self.marks3 = int(input("Please enter the marks : "))
        self.marks4 = int(input("Please enter the marks : "))
        self.marks5 = int(input("Please enter the marks : "))

        print(self)

    def calculate(self2):

        self2.total=self2.marks1+self2.marks2+self2.marks3+self2.marks4+self2.marks5

        self2.average=self2.total/5

        print(self2)

    def display(self3):

        print("The name is : ",self3.name)
        print("The Roll no is : ",self3.roll_no)
        print("The total marks is : ",self3.total)
        print("The Average is : ",self3.average)


obj=Student();
obj.input()
obj.calculate()
obj.display()

class student:
    def input(self):
        self.RollNumber=int(input("Please enter the roll number "))
        self.Name=input("Please enter the name ")
        self.marks1=int(input("Marks in first Subject : "))
        self.marks2 = int(input("Marks in second Subject : "))
        self.marks3 = int(input("Marks in third Subject : "))
        self.marks4 = int(input("Marks in fourth Subject : "))
        self.marks5 = int(input("Marks in fifth Subject : "))

        self.RollNumber = int(input("Please enter the roll number "))
        self.Name1 = input("Please enter the name ")
        self.marks11 = int(input("Marks in first Subject : "))
        self.marks21 = int(input("Marks in second Subject : "))
        self.marks31 = int(input("Marks in third Subject : "))
        self.marks41 = int(input("Marks in fourth Subject : "))
        self.marks51 = int(input("Marks in fifth Subject : "))


    def Cal(good):
        good.Total=good.marks1+good.marks2+good.marks3+good.marks4+good.marks5
        good.Total1 = good.marks11 + good.marks21 + good.marks31 + good.marks41 + good.marks51

        good.Average=good.Total/5
        good.Average1 = good.Total1 / 5

        good.Grade=''
        if(good.Average>70):
            good.Grade= 'A'
        elif(good.Average>64 and good.Average<74):
            good.Grade = 'B'
        elif(good.Average>40 and good.Average<59):
            good.Grade = 'C'
        else:
            good.Grade = 'D'

        good.Grade1 = ''
        if (good.Average1 > 70):
            good.Grade1 = 'A'
        elif (good.Average1 > 64 and good.Average1 < 74):
            good.Grade1 = 'B'
        elif (good.Average1 > 40 and good.Average1 < 59):
            good.Grade1 = 'C'
        else:
            good.Grade1 = 'D'

    def disp(bad):
        Indent=int(input("Please enter the roll number"))
        if(bad.RollNumber==1):
            print("The Roll Number is ",bad.RollNumber)
            print("The Name is ",bad.Name)
            print("The Total of all subjects are ",bad.Total)
            print("The Average is ",bad.Average)
            print("The Grade is ",bad.Grade)
        elif(bad.RollNumber==2):
            print("The Roll Number is ", bad.RollNumber)
            print("The Name is ", bad.Name1)
            print("The Total of all subjects are ", bad.Total1)
            print("The Average is ", bad.Average1)
            print("The Grade is ", bad.Grade1)





Knight=student()
Knight.input()
Knight.Cal()
Knight.disp()
class str:

    def input(s1):
        s1.String1=input("Please enter the string 1 :")
        s1.String2=input("Please enter the string 2 :")

    def Reverse(S1):
        S1.rev=S1.String1[::-1]
        S1.rev2=S1.String2[::-1]

    def Concat(self):
        self.con=(self.String1)+(self.String2)

    def Count(self):
        char = 0
        words = 1
        for i in self.String1:
            char+=1
            if(i==" "):
                words+=1
        char1 = 0
        words1 = 1
        for i in self.String2:
            char1+=1
            if(i==" "):
                words1+=1

        print("The Character in String one is ",char)
        print("The words in String one is ",words)
        print("The Characters in String two is ",char1)
        print("The words in String two is ",words1)




    def display(self):
        print("The reverse of string is ",self.rev)
        print("The reverse of another string is ",self.rev2)

        print("The Concatenation of the Strings are  ",self.con)



obj=str()
obj.input()
obj.Reverse()
obj.Concat()
obj.Count()
obj.display()




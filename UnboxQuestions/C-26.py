String=["The","Sun","Shines","Everyday","nitin"]
for i in String:
    case=i.casefold()
    rever=reversed(i)
if(list(case)==list(rever)):
        print("The word which is palindrome is\n",case)
else:
        print("No word is palindrome ")
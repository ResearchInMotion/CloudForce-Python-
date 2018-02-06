String="Friend is need when friend indeed"

charact=input("Please enter your character ")
value=charact in String

if(value==True):
    position=String.find(charact)
    print(position)
else:
    print("your value is not there ")
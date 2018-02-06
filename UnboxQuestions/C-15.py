String="aIbohPhoBiA"
String1=String.casefold()
Rev_String=reversed(String1)
if(list(String1)==list(Rev_String)):
    print("The string is palindrome")
else:
    print("no its not")
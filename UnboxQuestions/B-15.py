Input=input("please enter a charcater ")

isLowerInputaseVowel = (Input == 'a' or Input == 'e' or Input == 'i' or Input == 'o' or Input == 'u');


isUpperInputaseVowel = (Input == 'A' or Input == 'E' or Input == 'I' or Input == 'O' or Input == 'U');

if(isLowerInputaseVowel or isUpperInputaseVowel):
    print("this is a vowel")
else:
    print("this is a consonent")
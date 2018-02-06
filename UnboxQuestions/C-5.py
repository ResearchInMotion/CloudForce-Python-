String="your love is handmade for somebody like me"

vowels=0
consonents=0
digits=0

for i in String:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels+=1
    elif(i=='b' or i=='c' or i=='d' or i=='f' or i=='g' or i=='h' or i=='j' or i=='k' or i=='l' or i=='m' or i=='n' or i=='p' or i=='q' or i=='q' or i=='r' or i=='s' or i=='t' or i=='w' or i=='x' or i=='y' or i=='z'):
        consonents+=1

print(vowels)
print(consonents)
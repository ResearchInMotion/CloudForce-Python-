vals = [1,2,3,4,6,4,23,-8,-10]

num_Negative=0
num_Positive=0
num_eve=0
num_odd=0

for value in vals:
    if(value<0):
        num_Negative+=1


    elif(value>0):
        num_Positive+=1

    elif(value%2==0):
        num_eve+=1


    elif(value%2==1):
        num_odd+=1



print(num_Negative)
print(num_Positive)
print(num_eve)
print(num_odd)




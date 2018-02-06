String="Sahil nagpal is My name"
lower=0
upper=0
for i in String:
    if(i==i.lower()):
        lower+=1
    elif(i==i.upper()):
        upper+=1

print(lower)
print(upper)

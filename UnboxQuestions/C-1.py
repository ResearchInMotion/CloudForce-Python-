String="Krishna is the only god \n and i confirm that \t which actually no need to prove"

space=0
tabs=0
newline=0

for character in String:
    if (character ==" "):
        space += 1
    elif (character == '\t'):
        tabs += 1
    elif (character == '\n'):
        newline += 1




print(space)
print(tabs)
print(newline)

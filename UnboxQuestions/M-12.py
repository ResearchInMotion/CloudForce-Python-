fname=input("Please enter the path of the file name : ")
num_words=0

with open(fname , mode='r') as f:
    for line in f:
        words=line.split()
        num_words+=len(words)

print("The number of words are : ")
print(num_words)

with open("E:\Python_tecvision\File1.txt",mode='r') as infile:
    with open('E:\Python_tecvision\File2.txt',mode='w') as outfile:
        for val in infile:
            outfile.write(val)

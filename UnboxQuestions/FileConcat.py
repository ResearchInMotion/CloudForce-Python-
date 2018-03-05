filenames = ['E:\\Pythpn\\file1.txt', 'E:\\Pythpn\\file2.txt','E:\\Pythpn\\file3.txt']
with open('E:\Pythpn\output.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
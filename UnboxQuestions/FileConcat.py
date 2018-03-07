<<<<<<< HEAD
filenames = ['E:\\Pythpn\\file1.txt', 'E:\\Pythpn\\file2.txt','E:\\Pythpn\\file3.txt']
with open('E:\Pythpn\output.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
=======
filenames = ['E:\\Pythpn\\file1.txt', 'E:\\Pythpn\\file2.txt','E:\\Pythpn\\file3.txt']
with open('E:\Pythpn\output.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
>>>>>>> 3d758de8dcfac6789f74510b9bcc9a17ffcf52d7
            outfile.write(infile.read())
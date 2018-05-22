with open("D:\AddressEvaluation\AddressStandardization\infu\InfutorFile.txt") as inp, open("D:\AddressEvaluation\AddressStandardization\output.txt", 'w') as out:
    txt = inp.readline()
    txt = txt.replace('\r\n', '\n')
    out.write(txt)
print("Done")
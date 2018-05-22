with open("D:\AddressEvaluation\AddressStandardization\infu\InfutorFile.txt") as inp, open("D:\AddressEvaluation\AddressStandardization\output.txt", 'w') as out:
    txt = inp.read()
    txt = txt.replace('\n', '\r\n')
    out.write(txt)
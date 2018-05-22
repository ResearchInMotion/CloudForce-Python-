data = open("D:\AddressEvaluation\AddressStandardization\infu\InfutorFile.txt", "rb").read()
newdata = data.replace("\r\n", "\n")
if newdata != data:
            f = open("D:\AddressEvaluation\AddressStandardization\infu\InfutorFile.txt", "wb")
            f.write(newdata)
            f.close()
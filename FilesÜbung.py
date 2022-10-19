filewriter=open("dummy.txt", "wt")

filewriter.writelines("Nummer:    Name:    Datum: \n")
filewriter.writelines("Nummer:    Name:    Datum:")

filewriter.close()
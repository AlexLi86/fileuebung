filereader=open("dummy.txt", "rt")


text = filereader.read()
print(text)

lines = text.split("\n")

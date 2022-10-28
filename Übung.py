import datetime

file = open("Übung.txt", "at")
file2= open("Übung.txt", "rt")
current_date = datetime.date.today().strftime("%d.%m.%Y")
name=input("Geben Sie ihr Namen ein: ")

zähler=-1
text = file2.read()
lines = text.split("\n")

for line in lines:
    zähler+=1



zähler=str(zähler)
file.write("|  "+zähler+"|  "+current_date+"|  "+name+ "\n")
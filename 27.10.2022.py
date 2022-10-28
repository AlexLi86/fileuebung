file1=open("Wahrheitstabelle.txt", "wt")
aaa=input("Geben Sie AND, NAND, NOT, OR, NOR: ")
if aaa=="AND":
    file1.write("           AND           \n")
    file1.write("==========================\n")
    file1.write("A         |B           |X\n")
    file1.write("--------+--------+---------\n")
    a=True
    b=True
    x=a and b
    file1.write(str(a)+ " |"+str(b)+" |"+str(x)+"\n")
    a=True
    b=False
    x=a and b
    file1.write(str(a)+ " |"+str(b)+"|"+str(x)+"\n")
    a=False
    b=True
    x=a and b
    file1.write(str(b)+ " |"+str(a)+"|"+str(x)+"\n")
    a=False
    b=False
    x=a and b
    file1.write(str(b)+ "|"+str(b)+"|"+str(x)+"\n")
elif aaa=="NAND":
    file1.write("           NAND           \n")
    file1.write("==========================\n")
    file1.write("A         |B           |X\n")
    file1.write("--------+--------+---------\n")
    a=True
    b=True
    x=not(a and b)
    file1.write(str(a)+ " |"+str(b)+" |"+str(x)+"\n")
    a=True
    b=False
    x=not(a and b)
    file1.write(str(a)+ " |"+str(b)+"|"+str(x)+"\n")
    a=False
    b=True
    x=not(a and b)
    file1.write(str(b)+ " |"+str(a)+"|"+str(x)+"\n")
    a=False
    b=False
    x=not(a and b)
    file1.write(str(b)+ "|"+str(b)+"|"+str(x)+"\n")
elif aaa=="OR":
    file1.write("           OR           \n")
    file1.write("==========================\n")
    file1.write("A         |B           |X\n")
    file1.write("--------+--------+---------\n")
    a=True
    b=True
    x=a or b
    file1.write(str(a)+ " |"+str(b)+" |"+str(x)+"\n")
    a=True
    b=False
    x=a or b
    file1.write(str(a)+ " |"+str(b)+"|"+str(x)+"\n")
    a=False
    b=True
    x=a or b
    file1.write(str(b)+ " |"+str(a)+"|"+str(x)+"\n")
    a=False
    b=False
    x=a or b
    file1.write(str(b)+ "|"+str(b)+"|"+str(x)+"\n")
elif aaa=="NOR":
    file1.write("           NOR           \n")
    file1.write("==========================\n")
    file1.write("A         |B           |X\n")
    file1.write("--------+--------+---------\n")
    a=True
    b=True
    x=not(a or b)
    file1.write(str(a)+ " |"+str(b)+" |"+str(x)+"\n")
    a=True
    b=False
    x=not(a or b)
    file1.write(str(a)+ " |"+str(b)+"|"+str(x)+"\n")
    a=False
    b=True
    x=not(a or b)
    file1.write(str(b)+ " |"+str(a)+"|"+str(x)+"\n")
    a=False
    b=False
    x=not(a or b)
    file1.write(str(b)+ "|"+str(b)+"|"+str(x)+"\n")
elif aaa=="NOT":
    file1.write("           NOT           \n")
    file1.write("==========================\n")
    a=False
    x=not(a)
    file1.write(str(a)+ "|"+str(x)+"\n")
    b=True
    x=not(b)
    file1.write(str(b)+ " |"+str(x)+"\n")











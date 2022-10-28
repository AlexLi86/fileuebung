#import
import os

file_name= "dummy.txt"


if os.path.exists(file_name) == True:
    os.remove(file_name)
    print("removed " + file_name)
else:
    print("file " + file_name + " existiert nicht")
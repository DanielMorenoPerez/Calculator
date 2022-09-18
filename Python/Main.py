from Add import Add_funtion
from Subtract import subtract


print(" __________________________________")
print("| Calculator                       |")
print("|----------------------------------|")
print("|                                  |")
print("| Select your choice:              |")
print("|                                  |")
print("| -1  Add ->                       |")
print("| -2  Subtract ->                  |")
print("| -3  multiply ->                  |")
print("|                                  |")
print("|__________________________________|")

Awnser = input("")

if(Awnser == 1):
    Add_funtion()

if(Awnser == 2):
    subtract()



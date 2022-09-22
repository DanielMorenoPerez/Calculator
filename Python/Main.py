
from Add import Add_funtion
from Subtract import subtract
while 1:
    print(" __________________________________")
    print("| Calculator                       |")
    print("|----------------------------------|")
    print("|                                  |")
    print("| Select your choice:              |")
    print("|                                  |")
    print("| -1  Add ->                       |")
    print("| -2  Subtract ->                  |")
    print("| -3  multiply ->                  |")
    print("| -4  exit ->                      |")
    print("|__________________________________|")

    Awnser = int(input(""))

    if(Awnser == 1):
        Add_funtion()

    if(Awnser == 2):
        subtract()
    if(Awnser == 4):
        break



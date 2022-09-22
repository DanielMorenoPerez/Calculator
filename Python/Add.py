from operator import truediv
from Continue_change import Continue_Change

def Ask_first():
        print(" __________________________________")
        print("| Calculator                       |")
        print("|----------------------------------|")
        print("|                                  |")
        print("| Add your first number:           |")
        print("|__________________________________|")

        num1 = float(input(""))
        return num1
    


def Add_funtion():

    num1 = 0
    num2 = 0
    exit = 1
    num1 = Ask_first()
  
    while exit:
        print(" __________________________________")
        print("| Calculator                       |")
        print("|----------------------------------|")
        print("|                                  |")
        print("| Add your second number:          |")
        print("|__________________________________|")

        num2 = float(input(""))
        result = num1 + num2
        num1 = str(num1)
        num2 = str(num2)
        result = str(result)
        print(" _______________________________________")
        print("| Calculator                            |")
        print("|---------------------------------------|")
        print("|                                       |")
        print("| The result of " + num1 + " and " + num2 + " is " + result +"     |")
        print("|_______________________________________|")

        num1 = float(num1)
        num2 = float(num2)
        result = float(result)

        valor_continue = Continue_Change()

        if(valor_continue == True):
            num1 = result
        if(valor_continue == False):
            num1 = float(Ask_first())
        if(valor_continue == 0):
            break
        else:
            print(" _______________________________________")
            print("| Calculator                            |")
            print("|---------------------------------------|")
            print("|                                       |")
            print("| The answer you enter isnt sccepted    |")
            print("|_______________________________________|")



    
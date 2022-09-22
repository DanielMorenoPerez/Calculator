from Add import Ask_first
from Continue_change import Continue_Change

def subtract():

    def operation_Subtract(num1):

        while 1:
            print(" __________________________________")
            print("| Calculator                       |")
            print("|----------------------------------|")
            print("|                                  |")
            print("| Add your second number:          |")
            print("|__________________________________|")

            num2 = float(input(""))

            result = num1 - num2
            num1 = str(num1)
            num2 = str(num2)
            result = str(result)
            print(" _______________________________________")
            print("| Calculator                            |")
            print("|---------------------------------------|")
            print("|                                       |")
            print("| The result of " + num1 + " minus " + num2 + " is " + result +"   |")
            print("|_______________________________________|")

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


        num = Ask_first()
        operation_Subtract(num)

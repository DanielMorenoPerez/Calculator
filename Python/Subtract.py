def subtract():

    num1 = 0
    num2 = 0

    print(" __________________________________")
    print("| Calculator                       |")
    print("|----------------------------------|")
    print("|                                  |")
    print("| Add your first number:           |")
    print("|__________________________________|")

    num = float(input(""))

    def operation_Subtract(num1):

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

        operation_Subtract(num)

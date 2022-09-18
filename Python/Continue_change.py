def Continue_Change():

    return_value = True
    print(" _______________________________________")
    print("| Calculator                            |")
    print("|---------------------------------------|")
    print("|                                       |")
    print("| Do you want to continue with this     |")
    print("| number or change to another           |")
    print("|                                       |")
    print("| y: yes                                |")
    print("| n: change to other                    |")
    print("| e: exit                               |")
    print("|_______________________________________|")

    select = input("")

    if(select == 'y'):
        return_value = True
    if(select == 'n'):
        return_value = False
    if(select == 'e'):
        return_value = 0
    return return_value


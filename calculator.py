def help_screen():
    print("Add : adds two numbers")
    print("Substract : Substract two numbers")
    print("Print: Displays the result of the latest operation")
    print("Help: Displays this help screen")
    print("Quit: Exits the program")

#menu

def menu():
    return input(" ==> A) Add S) Substraction P) print H) Help Q)Quit : ")

def main():
    result = 0.0
    done= False
    while not done:
        choice = menu()

        if choice == "A" or choice=="a":  #შეკრება
            arg1 = float(input("Enter arg 1: "))
            arg2 = float(input("Enter arg 2:  "))
            result = arg1 + arg2
            print(result)
        elif choice == "S" or choice=="s":  #გამოკლება
            arg1 = float(input("Enter arg 1: "))
            arg2 = float(input("Enter arg 2:  "))
            result = arg1 - arg2
            print(result)
        elif choice == "P" or choice=="p":  #print
            print(result)
        elif choice == "Q" or choice=="q":  #quit
            done= True
        elif choice == "H" or choice=="h":  #help
            help_screen()
main()
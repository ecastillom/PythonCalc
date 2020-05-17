import os

def clear():
    os.system('cls')

def separator():
    print("-" * 30)
    
def breakline():
    print(" " * 30)

def print_menu():
    separator()
    print("Welcome to PyCal")
    separator()

    print("[1] - Add")
    print("[2] - Substract")
    print("[3] - Multiply")
    print("[4] - Divide")
    print("[x] - Close")


def sum(num1, num2):
    return num1 + num2

def rest(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "E"
    else:
        return num1 / num2

opc = ""

while(opc != 'x'):
    print_menu()
    
    breakline()
    opc = input("Please select an option: ")
    breakline()

    if(opc == "x"):
        break

    num1 = float(input("Type Number 1: "))
    num2 = float(input("Type Number 2: "))
    breakline()

    if(opc == "1"):
        result = sum(num1, num2)
        print("Result: " + str(result))
    
    elif(opc == "2"):
        result = rest(num1, num2)
        print("Result: " + str(result))

    elif(opc == "3"):
        result = mult(num1, num2)
        print("Result: " + str(result))

    elif(opc == "4"):
        result = div(num1, num2)
        if result == "E":
            print("Error!! You Can't Divided by Zero")
        else:
            print("Result: " + str(result))

    breakline()
    input("Press Enter: ")
    clear()

print("I will Back")
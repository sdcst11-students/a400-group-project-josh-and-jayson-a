#!python3
# Volume Calculator
# Feel free to rename your variables
    

def title():
    print("============")
    print("= CALCULATOR =")
    print("============")
    return None

def help():
    print("_________________________\n========\n= HELP =\n========\n+ = addition\n- = subtraction\nx = multiplication\n/ = division\n** = exponent\n_________________________\n")

def instructions():
    print("__________________________________________________\n================\n= INSTRUCTIONS =\n================\nStart by entering a number followed by +,-,/,x,**, then enter your second number.\nThe calculator will print the answer.\nYou may continue off your answer or close the program.\n__________________________________________________\n")

def number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

title()
instructions()

num = float(input("Enter a number: "))

while True:
    math1 = input("Enter an operation (+, -, x, /, **): ")

    if number(math1):
        print("Invalid input. Please enter a valid operation.")
        continue

    num2 = float(input("Enter the next number: "))

    if math1 == "+":
        x = num + num2
    elif math1 == "x":
        x = num * num2
    elif math1 == "**":
        x = num ** num2
    elif math1 == "-":
        x = num - num2
    elif math1 == "/":
        x = num / num2
    else:
        print("Invalid operation. Please enter a valid operation.")
        continue

    print(f"= {x}")
    num = x












    









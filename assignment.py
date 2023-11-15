#!python3
# Volume Calculator
# Feel free to rename your variables
    

def title():
    print("============")
    print("=CAlCULATOR=")
    print("============")
    return None

def help():
    print("+ = addition\n- = subtraction\nx = multiplication\n/ = division\n** = exponent")

def instruct():
    print("Start by entering a number followed by +,-,/,x,**, then enter your second number.\nThe calculator will print the answer.\nYou may continue off your answer or type 'quit'.")

def instructions():
    menu = input('Type "instructions" "help" or "skip": ')
    if menu == "instructions":
        instruct()
    if menu == "help":
        help()
    if menu == "skip":
        pass
        return None


        
            

title()
instructions()
num = float(input(""))
while True:
    math1 = (input(""))
    num2 = float(input(""))
    
    
    if math1 == "+":
        x = num + num2
        num = x
    if math1 == "x":
        x = num * num2
        num = x
    if math1 == "**":
        x = num **num2
        num = x
    if math1 == "-":
        x = num - num2
        num = x
    if math1 == "/":
        x = num / num2
        num = x
    
    print(f"= {x}")

    
    
    

    

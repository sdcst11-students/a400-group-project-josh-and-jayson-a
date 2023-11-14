#!python3
# Volume Calculator
# Feel free to rename your variables
    

def title():
    print("============")
    print("=CAlCULATOR=")
    print("============")
    return None

def instructions():
    help = input('Type "instructions" "help" or "skip": ')
    if help == "instructions" or "instruction":
        print("Start by entering a number followed by +,-,/,x,**, then enter your second number.\nThe calculator will print the answer.\nYou may continue off your answer or type 'quit'.")
    if help == "help":
        print("+ = addition\n- = subtraction\nx = multiplication\n/ = division\n** = exponent")
    if help == "skip":

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

    
    
    

    

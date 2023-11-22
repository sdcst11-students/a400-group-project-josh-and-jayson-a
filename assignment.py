#!python3
# Volume Calculator
# Feel free to rename your variables
    

def title():
    print("============")
    print("=CAlCULATOR=")
    print("============")
    return None


def help():
    print("_________________________\n========\n= HELP =\n========\n+ = addition\n- = subtraction\nx = multiplication\n/ = division\n** = exponent\n_________________________\n")


def instruct():
    print("__________________________________________________\n================\n= INSTRUCTIONS =\n================\nStart by entering a number followed by +,-,/,x,**, then enter your second number.\nThe calculator will print the answer.\nYou may continue off your answer or type 'quit'.\n__________________________________________________\n")
    
def instructions():
    while True:
        menu = input('Type "instructions" "help" or "skip": ')


        if menu != "instructions" and menu != "help" and menu != "skip":
            print("invalid, try agian")
        elif menu == "instructions":
            instruct()
            
        elif menu == "help":
            help()
            
        elif menu == "skip":
            print("ok :)")
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











    









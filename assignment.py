#!python3
# Volume Calculator
# Feel free to rename your variables
    

def title():
    print("============")
    print("=CAlCULATOR=")
    print("============")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

import math
def main():
    calc = True
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
        



        
           
        
        
            
            
            
            

        
        
            



        title()
    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()

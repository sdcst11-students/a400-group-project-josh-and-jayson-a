#!python3
# Volume Calculator
# Feel free to rename your variables
    

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

#for interest rates multiply any number by 0.0042 and then by the time period you want


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
        





        print(f"={x}")
        if num == "quit":
            num = str(num)
            False
        if math1 == "quit":
            False
        if num2 == "quit":
            num2 = str(num2)
            False
            return
        
        
        
        
            
            
            

        
        
            



    title()
    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()

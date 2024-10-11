#this program will define a function f(x) that returns x**3 + 8. In the main function of the program, call f(x) with x = 9 and print the result
import numpy as np
x=9
def f(x):
    return x**3 + 8
print(f(x))

def main():
    if (f(x)>27):
        print("yay!")
    else:
        print("Nay!")
    
if __name__=="__main__":
    main()
    

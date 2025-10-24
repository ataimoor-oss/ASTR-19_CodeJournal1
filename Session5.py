#Session 5
#Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand entries. Follow the basic Python program structure, including a main program function.

import numpy as np 
import math 

def main():
    x_val = np.linspace(0, 2, 1000)
    print("x\t sin(x)")
    for x in x_val: 
        print(f"{x:.3f}\t {math.sin(x):.3f}")

if __name__ == "main":
    main()
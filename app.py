import sympy as sp
from reimann import reimann
from midpoint import midpoint
from trapezoid import trapezoid
import numpy as np
import matplotlib.pyplot as plt
import plotter
import sys

def fail(msg):
    print(msg)
    sys.exit()

x=sp.Symbol('x')
print("------------------Welcome------------------")

try:
    expr=sp.sympify(input("Enter the intergrand: "))
    f=sp.lambdify(x,expr)
except (sp.SympifyError, SyntaxError):
    fail("Invalid Mathematical expression")


try:
    a=float(input("Enter the lower limit: "))
    b=float(input("Enter the upper limit: "))
    n=int(input("Enter the resolution: "))
except ValueError:
    fail("Invalid numeric input")


if (n<=0):
    fail("Resolution must be a positive integer")

s=0
if (a>b):
    s=1
    a,b=b,a

def return_val(c):
    if (c==1):
        res=reimann(f,a,b,n)
    elif (c==2):
        res=midpoint(f,a,b,n)
    elif (c==3):
        res=trapezoid(f,a,b,n)
    if s==1:
        res=-res
    return res

def graph(c):
    if (c==1):
        plotter.plot_reimann(f,a,b,n)
    elif (c==2):
        plotter.plot_midpoint(f,a,b,n)
    elif (c==3):
        plotter.plot_trapezoid(f,a,b,n)

print("------------------Choose Mode------------------")
print("1. Computing")
print("2. Computing + Graphing")
print("3. Comparison")

try:
    m=int(input("Enter Mode[1-3]: "))
    
except ValueError:
    fail("Invalid Mode: Mode must be a number")
    
if m<1 or m>3:
    fail("Invalid Mode: Mode must strictly be between 1 and 3")

if (m==1 or m==2):
    print("------------------Choose Method------------------")
    print("1. Riemann")
    print("2. Midpoint")
    print("3. Trapezoid")
    
    try:
        c=int(input("Enter Method[1-3]: ")) 
    except ValueError:
        fail("Invalid Choice: Choice must be a number")
    
    if c<1 or c>3:
        fail("Invalid Choice: Choice must strictly be between 1 and 3")
    res=return_val(c)
    print(f"Result: {res:.3f}")
    if (m==2):
        graph(c)
        plt.show()

elif (m==3):
    fig,axs=plt.subplots(1,3,figsize=(15,4))

    print(f"Reimann: {return_val(1):.3f}")
    plotter.plot_reimann(f, a, b, n, axs[0])
    axs[0].set_title("Riemann")

    print(f"Midpoint: {return_val(2):.3f}")
    plotter.plot_midpoint(f, a, b, n, axs[1])
    axs[1].set_title("Midpoint")

    print(f"Trapezoid: {return_val(3):.3f}")
    plotter.plot_trapezoid(f, a, b, n, axs[2])
    axs[2].set_title("Trapezoid")

    plt.tight_layout()
    plt.show()


    
    
    

    



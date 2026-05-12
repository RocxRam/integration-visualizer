import numpy as np
import matplotlib.pyplot as plt

def plot_func(f,a,b,ax):
    x=np.linspace(a,b,1000)
    y=f(x)
    ax.plot(x,y)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

def plot_reimann(f,a,b,n,ax):
    dx=(b-a)/n
    plot_func(f,a,b,ax)
    for i in range(n):
        x=a+i*dx
        ax.bar(x,f(x),width=dx,align='edge',alpha=0.3)

def plot_midpoint(f,a,b,n,ax):
    dx=(b-a)/n
    plot_func(f,a,b,ax)
    for i in range(n):
        x=a+i*dx+dx/2
        ax.bar(x,f(x),width=dx,alpha=0.3)

def plot_trapezoid(f,a,b,n,ax):
    dx=(b-a)/n
    plot_func(f,a,b,ax)
    for i in range(n):
        x=a+i*dx
        xn=x+dx
        y=f(x)
        yn=f(xn)
        ax.plot([x,xn],[y,yn])
        ax.plot([x,x],[0,y])
        ax.plot([xn,xn],[0,yn])

    

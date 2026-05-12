def trapezoid(f,a,b,n):
    dx=(b-a)/n
    t=0
    for i in range(n):
        x=a+i*dx
        xn=x+dx
        t+=f(x)+f(xn)
    return t*dx/2

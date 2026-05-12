def midpoint(f,a,b,n):
    dx=(b-a)/n
    t=0
    for i in range(n):
        x=a+(i+1/2)*dx
        t+=f(x)
    return t*dx

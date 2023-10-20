"""
Practica 3 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import *
from matplotlib.pyplot import *

""" Ejercicio 1 """

# Los parametros de puntofijo son:
# La funcion de iteracion g
# La semilla x0
# La precision epsilon
# El numero maximo de iteraciones

# Se para cuando abs(xn - x(n-1)) <= epsilon

def puntofijo(g,x0,eps,nmax):
    error = eps + 1
    k = 0
    while (error > eps and k < nmax):
        x1 = g(x0) 
        error = abs(x1 - x0)
        x0 = x1
        k = k + 1
    if k == nmax:
        print("Se alcanza el número máximo de iteraciones")
        print("El último valor calulado es",x1)
    else:
        print("Se alcanza la precisión requerida en",k,"iteraciones")
        print("El último valor calulado es",x1)
    return x1

""" Ejercicio 2 """ 

# Usar puntofijo para calcular la raix de x - e^(-x) = 0 con los valores
# x0 = 0,5, epsilon = 10^(-7) y nmax = 100 usando el metodo de punto fijo
# y el metodo de newton

""" Apartado A """    

def g2a(x):
    return exp(-x)

puntofijo(g2a,0.5,1e-7,100)

""" Apartado B """

def g2b(x):
    return x - (x - exp(-x))/(1 + exp(-x))

puntofijo(g2b,0.5,1e-7,100)

""" Ejercicio 3 """ 

# Usar puntofijo para calcular la raix de K = x - alfasen(x) con los valores
# alfa = 0,093, k = 2/3, x0 = 0,5 , epsilon = 10^(-7) y nmax = 100 
# usando el metodo de Xn+1 = K + alfasen(Xn) y el metodo de newton

""" Apartado A """    

def g3a(x):
    return 2/3 + 0.093*sin(x)

# puntofijo(g3a,0.5,1e-7,100)

""" Apartado B """    

def g3b(x):
    return x - (2/3 + 0.093*sin(x) - x)/(0.093*cos(x) - 1)

# puntofijo(g3b,0.5,1e-7,100)

""" Ejercicio 4 """ 

# Aproximar la unica raiz de la ecuacion cos(x) - x = 0
# con x0 = 0,5, epsilon = 10^(-7) y nmax = 100 usando los metodos 
# Xn+1 = cos(xn) y metodo de newtown

"""" Apartado A """

def g4a(x):
    return cos(x)

#puntofijo(g4a,0.5,1e-7,100)

""" Apartado B """

def g4b(x):
    return x - (cos(x) - x)/(-sin(x) - 1)

# puntofijo(g4b,0.5,1e-7,100)

""" Ejercicio 5 """

# Analogo a los anteriores

""" Ejercicio 6 """ 

""" Apartado A """

# Modificar puntofijo para que utilice como criterio de parada
# abs(fxn)) <= epsilon

def puntofijo2(f,g,x0,eps,nmax):
    error = eps + 1
    k = 0
    while (error > eps and k < nmax):
        x1 = g(x0)
        error = abs(f(x1))
        x0 = x1
        k = k + 1
    if k == nmax:
        print("Se alcanza el número máximo de iteraciones")
        print("El último valor calulado es",x1)
    else:
        print("Se alcanza la precisión requerida en",k,"iteraciones")
        print("El último valor calulado es",x1)
    return x1

""" Apartado B """

# Para f (x) = x + (x − 1)e^x, comprobar que tiene una única raíz en el intervalo [0, 1] 
# dibujando su gráfica.

def f6b(x):
    return x + (x-1)*exp(x)

# x = linspace(0,1,100)
# y = f6b(x)
# plot(x,y,"r",x,0*x)
# xlabel("Eje X")
# ylabel("Eje Y")
# show()

""" Apartado C """

# Utilizar el programa obtenido en el primer apartado para aproximar dicha raíz 
# con el método de Newton, una semilla adecuada obtenida a partir 
# de la gráfica y epsilon = 10−8

def g6c(x):
    return x - f6b(x)/(1 + x*exp(x))

# puntofijo2(f6b,g6c,0.7,10e-8,100)

""" Apartado D """

# Analogo a los anteriores




""" Metodo de Newton """

def newton(f1,f2,a,b,x0,eps):
    print()
    print("----- MÉTODO DE NEWTON -----")
    print("%1s %13s %13s" % ("k", "xk", "f(xk)"))
    def newton2(f1,f2,a,b,x0,eps,k):
        if f2(x0) == 0:
            return "Error, la derivada en xk vale 0"
        else:
            x1 = x0- f1(x0)/f2(x0)
            if x1 < a:
                print("Error: xk <",a)
            elif x1 > b:
                print("Error: xk >",b)
            elif f1(x1) == 0:
                print("La raiz es:" ,x1)
                return x1
            else:
                if abs(x0 - x1) < eps:
                    print("%1i %13.10f %13.10f" % (k, x1, f1(x1)))
                    return x1
                else:
                    print("%1i %13.10f %13.10f" % (k, x1, f1(x1)))
                    newton2(f1,f2,a,b,x1,eps,k+1)
                            
    return newton2(f1,f2,a,b,x0,eps,0)   


""" Metodo de Haley """

# f1 es la funcion, f2 es la primera derivada y f3 la segunda derivada

def haley(f1,f2,f3,a,b,x0,eps):
    print()
    print("----- MÉTODO DE HALEY -----")
    print("%1s %13s %13s" % ("k", "xk", "f(xk)"))
    def haley2(f1,f2, f3,a,b,x0,eps,k):
        if f2(x0) == 0:
            return "Error, la derivada en xk vale 0"
        else:
            x1 = x0 - (2*f(x0)f2(x0))/(2((f2(x0))**2 ) - f(x0)*f3(x0))
            if x1 < a:
                print("Error: xk <",a)
            elif x1 > b:
                print("Error: xk >",b)
            elif f1(x1) == 0:
                print("La raiz es:" ,x1)
                return x1
            else:
                if abs(x0 - x1) < eps:
                    print("%1i %13.10f %13.10f" % (k, x1, f1(x1)))
                    return x1
                else:
                    print("%1i %13.10f %13.10f" % (k, x1, f1(x1)))
                    haley2(f1,f2,f3,a,b,x1,eps,k+1)
                            
    return haley2(f1,f2,f3,a,b,x0,eps,0)
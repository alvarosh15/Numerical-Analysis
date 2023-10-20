"""
Examen septiembre 19/20 modelo 1 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

""" Ejercicio 1 """

# La funcion log(x) - 1/x tiene una unica raiz l que se desea aproximar 

def f(x):
    return log(x) - (1/x)

""" Apartado A) """

# Con ayuda de plot halle un intervalo de longitud 1 que contenga a l

# x = linspace(0.1, 6, 100)
# y = f(x)
# plot = (x, y)
# grid("on")
# show()

print("Vemos que el intervalo donde está l es (1,2) y es un intervalo de longitud 1.")

""" Apartado B) """

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

def fm1(x):
    return exp(1/x)

print("Aproximacion de la raiz l mediante fm1 = e^(1/x)")
puntofijo2(f,fm1,1.5, 1e-10, 500)

def fm2(x):
    return 1/log(x)

print("Aproximacion de la raiz l mediante fm2 = 1/log(x)")
# puntofijo2(f,fm2,1.5, 1e-10, 500)
print("El segundo metodo no es convergente")

def fm3(x):
    return (x**2*(1-log(x)) + 2*x)/(x + 1)

print("Aproximacion de la raiz l mediante fm3 = (x**2*(1-log(x)) + 2x)/(x + 1)")
puntofijo2(f,fm3,1.5, 1e-10, 500)

print("El metodo dos no es convergente, de entre el primero y el tercero, el tercero es mucho mas rapido")


""" Ejercicio 2 """

# Aproximar raiz cubica de 10 y raiz cubica de 100 usando interpolacion

def tabla_diferencias_divididas(x,y):
    """ Calcula la tabla completa de las diferencias divididas a partir de los datos
    x e y. Devuelve una matriz (df) triangular inferior que en la columna k-esima
    contiene las diferencias de orden k."""
    n= len(y)
    df=zeros([n,n])
    df[:,0]=y
    yn=y
    for i in range(0, len(x)-1):
        dx=x[i+1: len(x)]-x[0:n-(i+1)]
        yn=diff(yn)/dx
        df[i+1:n,i+1]=yn
    return df
    
def eval_forma_newton(x,y,z_0):
    """ Calcula en primer lugar el polinomio de interpolacion de Lagrange que interpola 
    los datos x e y mediante la formula de Newton y lo evalua en z0."""  
    n= len(y)
    df=tabla_diferencias_divididas(x,y)
    peval=df[0,0]
    prod=1.0
    for i in range(1,n):
        prod=prod*(z_0-x[i-1])
        peval=peval+df[i,i]*prod
    return peval    

def eval_forma_newton_horner(x,y,z0):   
    n = len(y)
    df = tabla_diferencias_divididas(x,y)
    cn = df[n-1,n-1]
    for i in range (n-2,-1,-1):
        cn = cn*(z0-x[i])+df[i,i]
    return cn

""" Apartado A """

# Observe que los puntos del plano (n^3, n) estan en la grafica de 
# raiz cubica de x. Escriba un programa que permita evaluar en cualquier punto
# el polinomio p de grado menor o igual que 4 que interpola dichos puntos

y = linspace(1, 5, 5)
x = y**3
plot(x, y, "b")
grid("on")
show()

def polinomio(c):
    return eval_forma_newton_horner(x, y, c)

""" Apartado B """ 

# Con ayuda de plot dibuje las graficas de f y p en [1, 125]

x1 = linspace(1, 125, 200)
y1 = polinomio(x1)
plot(x1, y1, "b", x1, x1**(1/3), "red")
grid("on")
show()

print("f viene de color rojo y p de color azul")

""" Apartado C """

# Aproxime raiz cubica de 10 y raiz cubica de 100 mediante p(10) y p(100), 
# respectivamente. Compare con las aproximaciones que se obtienen usando 
# el operador ** de python.

puntos = array([10,100])
aproximar = polinomio(puntos)

print("La aproximacion de 10^(1/3) con el polinomio de interpolacion es ", aproximar[0], "y el error cometido es ", 10**(1/3) - aproximar[0])

print("La aproximacion de 100^(1/3) con el polinomio de interpolacion es ", aproximar[1], "y el error cometido es ", 100**(1/3) - aproximar[1])

""" Apartado D """

# Repetir lo anterior con interpolacion spline cubica, ¿Cual es mejor? 

def intcubic(x, y): 
    pol = interp1d(x, y, "cubic")
    return pol

pol = intcubic(x1, y1)
print("La aproximacion ", pol(10), " el error ", 10**(1/3) - pol(10))
print("La aproximacion ", pol(100), " el error ", 100**(1/3) - pol(100))






















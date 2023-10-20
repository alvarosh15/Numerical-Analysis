"""
Examen septiembre 17/18 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

""" Ejercicio 1 """

def f(x): 
    return x + (x - 1)*exp(x)

""" Apartado A """

# Comprobar que tiene una unica raiz en [0,1]

x = linspace(0, 1, 100)
y = f(x)
plot(x, y, "b", x, 0*x, "black")
grid("on")
show()

""" Apartado B """

# Aproximar dicha raiz usando el metodo de Newton escogiendo semilla
# adecuada y epsilon = 1e-u8

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

def df(x):
    return 1 + exp(x) + (x - 1)*exp(x)

def fnewton(x):
    return x - f(x)/df(x)

puntofijo2(f, fnewton, 0.5, 1e-8, 100)

""" Apartado C """

# Usar otro metodo de punto fijo con la misma semilla y epsilon 

def fc(x):
    return 1 - x/exp(x)

puntofijo2(f, fc, 0.5, 1e-8, 100)

""" Ejercicio 2 """

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

def eval_forma_newton_horner(x,y,z0):   
    n = len(y)
    df = tabla_diferencias_divididas(x,y)
    cn = df[n-1,n-1]
    for i in range (n-2,-1,-1):
        cn = cn*(z0-x[i])+df[i,i]
    return cn

""" Apartado A """

# Calcular el polinomio de interpolacion de f^-1

x = array([1.533, 0.576, -0.554, -1.11, -2.1])
y = linspace(0, 2, 5)

def polinomio(c):
    return eval_forma_newton_horner(x, y, c)

""" Apartado B """

# Dibuja la grafica de p en [-2.1, 1.533] 

x2 = linspace(-2.1, 1.533)
y2 = polinomio(x2)
plot(x2, y2, "blue", x2, 0*x2, "black", x, y, "ro")

""" Apartado C """

# Evalue p en 0 para aproximar l 

print("La aproximacion de p en 0 para aproximar l es ", polinomio(0))
















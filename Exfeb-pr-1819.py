"""
Examen febrero 18/19 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

""" Ejercicio 1 """

" Apartado A "

# Con ayudad de plot encuentra un intervalo de longitud 1 donde esté l

def f(x):
    return exp(2*x) + 3*x + 2

x = linspace(-1, 0, 100)
y = f(x)
plot(x,y, "red", x, 0*x, "black")
grid("on")
show()

print("El intervalo donde f tiene sol es [-1, 0] que es de longitud 1")

""" Apartado B """

# Aplica metodo de Newton con test de parada 1e-12 y semilla el punto medio de I

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

def df(x):
    return 2*exp(2*x)+3

def fnewton(x):
    return x - (f(x)/df(x))

puntofijo(fnewton, -0.5, 1e-12, 100)

""" Apartado C """ 

# Aplicar el apartado B con el metodo de Haley 

def ddf(x):
    return 4*exp(2*x)

def fhaley(x):
    return x - (2*f(x)*df(x))/(2*(df(x)**2-f(x)*ddf(x)))

puntofijo(fhaley, -0.5, 1e-12, 100)

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

# Estime la poblacion de 1936 usando el polinomio que interpola los datos de la tabla

x1 = linspace(1910, 1990, 9)
y1 = array([529.575, 562.525, 609.613, 688.193, 756.083, 781.690, 853.579, 1025.609, 1160.843])

def polinomio(c):
    return eval_forma_newton_horner(x1, y1, c)

print("La poblacion estimada en 1936 es ", polinomio(1936))

""" Apartado B """

# Interpolacion linear

def intlin(x, y):
    pol = interp1d(x, y, kind = "linear")
    return pol

pol = intlin(x1, y1)

print("La poblacion estimada mediante lineal a trozos en 1936 es ", pol(1936))

""" Apartado C """

# Poner todos los datos anteriores en una grafica 

y2 = polinomio(x1)
y3 = pol(x1)
plot(x1, y1, "ro", x1, y2, "green", x1, y3, "b")
grid("on")
show()

























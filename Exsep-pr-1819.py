"""
Examen septiembre 18/19 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

""" Ejercicio 1 """

""" Apartado A """

def puntofijo(g,x0, nmax):
    k = 0
    print("%11s %11s %11s" % ("k", "xn", "g(xn)"))
    while (k < nmax):
        print("%11i %11.8f %11.8f" % (k, x0, g(x0)))
        x1 = g(x0) 
        x0 = x1
        k = k + 1
    if k == nmax:
        print("Se alcanza el número máximo de iteraciones")
        print("El último valor calulado es",x1)
    return x1

""" Apartado B """

# Aplicar tres metodos de punto fijo a f

def f1(x):
    return -exp(x)

puntofijo(f1, -0.5, 11)



def f2(x):
    return log(-x)

# puntofijo(f2, -0.5, 11)

def f3(x):
    return ((x-1)*exp(x))/(1 + exp(x))

puntofijo(f3, -0.5, 11)

""" Apartado C """
"""
def f(x):
    return exp(x) + x

x = linspace(-1, 0, 200)
yid = f(x)
y1 = f1(x)
plot(x, yid, "blue", x, y1, "green", x, 0*x, "black") 
axis([-1, 0, -1, 0])

y2 = f2(x)
plot(x, yid, "blue", x, y2, "green",  x, 0*x, "black") 
axis([-1, 0, -1, 0])

y3 = f3(x)
plot(x, yid, "blue", x, y3, "green", x, 0*x, "black") 
axis([-1, 0, -1, 0])"""

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

# Aproxima el valor del seno 

x = array([1.047, 1.134, 1.221, 1.308, 1.396])
y = array([0.86592661, 0.90611159, 0.93944253, 0.96566732, 0.98476198])

def polinomio(c):
    return eval_forma_newton_horner(x, y, c)

print("El valor aproximado del seno 1.2 es ", polinomio(1.2))

# ESTA "MAL" HAY QUE HACERLO PARA N = 1, 2, 3, 4... es decir usando
# el primer punto, el segundo, etc...

""" Apartado B """

print("El error aproximado del seno 1.2 es ", abs(sin(1.2) - polinomio(1.2)))

""" Apartado C """

xc = linspace(1, 1.4)
yc = polinomio(xc)
plot(xc, yc, "black", xc, sin(xc), "green")
show()





















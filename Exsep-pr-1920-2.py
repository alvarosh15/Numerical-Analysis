"""
Examen septiembre 19/20 modelo 2 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

""" Ejercicio 1 """

def f(x): 
    return log(-x) + 1/x

""" Apartado A """

# Con ayuda de plot hallar un intervalo de longitud 1 que contenga a l

x = linspace(-2, -1)
y = f(x)
plot(x, y, "b", x, 0*x, "black")

print("Es facil ver que el intervalo buscado es [-2, -1]")

""" Apartado B """

# Aplicar los siguientes metodos de punto fijo 

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

def f1(x): 
    return -exp(-1/x)

def f2(x): 
    return -1/(log(-x))

def f3(x):
    return ((x**2)*(1-log(-x))-2*x)/(x-1)

puntofijo2(f, f1, -1.5, 1e-10, 500)
#puntofijo2(f, f2, -1.5, 1e-10, 500)
puntofijo2(f, f3, -1.5, 1e-10, 500)

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

# Aproximar raiz de 2 y raiz de 20

""" Apartado A """

y = linspace(1, 5, 5)

x = y**2

def polinomio(c):
    return eval_forma_newton_horner(x, y, c)


""" Apartado B """ 

x1 = linspace(1, 25, 100)
y1 = polinomio(x1)
y2 = sqrt(x1)
plot(x1, y1, "blue", x1, y2, "green")
show()

""" Apartado C """

print("La aproximacion de raiz de 2 es ", abs(sqrt(2) - polinomio(2)))


print("La aproximacion de raiz de 20 es ", abs(sqrt(20) - polinomio(20)))

""" Apartado D """ 

# Repetir con interpolacion cubica 

def intcub(x, y):
    pol = interp1d(x, y, kind = "cubic")
    return pol 

pol = intcub(x, y)

plot(x1, pol(x1), "blue", x1, y2, "green")


print("La aproximacion de raiz de 2 es ", abs(sqrt(2) - pol(2)))


print("La aproximacion de raiz de 20 es ", abs(sqrt(20) - pol(20)))































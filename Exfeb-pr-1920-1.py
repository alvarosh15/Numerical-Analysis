"""
Examen febrero 19/20 modelo 1 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

""" Ejercicio 1 """

def f(x):
    return x**6 - 6*x**4 + 12*x**2 - 8

# La unica solucion positiva es raiz de 2

""" Apartado A """

# Aplicar metodo de punto fijo, se debe mostrar en pantalla 
# n, xn, en, en/e(n-1)

def puntofijo2(f,g,x0,eps,nmax):
    error = eps + 1
    k = 0
    print("%6s %11s %20s %20s" % ("n", "xn", "en", "en/en-1"))
    while (error > eps and k < nmax):
        x1 = g(x0)
        error = abs(f(x1))
        k = k + 1
        print("%6i %11.8f %20.16f %20.16f" % (k, x1, error, error/abs(f(x0))))      
        x0 = x1
    if k == nmax:
        print("Se alcanza el número máximo de iteraciones")
        print("El último valor calulado es",x1)
    else:
        print("Se alcanza la precisión requerida en",k,"iteraciones")
        print("El último valor calulado es",x1)
    return x1

""" Apartado B """

def df(x): 
    return 6*x**5 - 24*x**3 + 24*x 

def fnewton(x):
    return x - (f(x)/df(x))

puntofijo2(f, fnewton, 1.5, 1e-12, 500)

# Como la constante asintotica del metodo es 0.29 el orden es al menos 2 
# Es el orden esperado ya que el orden del metodo de newton es 2 

""" Apartado C """

def fc(x): 
    return x - 3*f(x)/df(x)

puntofijo2(f, fc, 1.5, 1e-12, 500)

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

    
def polinomio(y, c):
    return eval_forma_newton_horner(x, y, c)

""" Apartado A """

# Interpolacion lineal a trozos de sup e inf y ponerlo en una grafica a ambos

x = array([0, 0.025, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

def intlin(y):
    pol = interp1d(x, y, kind = "linear")
    return pol

def intcubic(y):
    pol = interp1d(x, y, kind = "cubic")
    return pol

ys = array([0, 0.0250, 0.0376, 0.0563, 0.0812, 0.0962, 0.1035, 0.1033, 0.0950, 0.0802, 0.0597, 0.0340, 0])

pol1 = intlin(ys)

yi = array([0, -0.0052, -0.0060, -0.0045, -0.0016, 0.0010, 0.0036, 0.0070, 0.0121, 0.0170, 0.0199, 0.0178, 0])

pol2 = intlin(yi)

plot(x, pol1(x), "blue", x, pol2(x), "green", x, ys, "ro", x, yi, "ro")
grid("on")
show()

""" Apartado B """

# Analogo a A pero con interpolacion cubica

pol3 = intcubic(ys)

pol4 = intcubic(yi)

plot(x, pol3(x), "blue", x, pol4(x), "green", x, ys, "ro", x, yi, "ro")
grid("on")
show()

""" Apartado C """

pol5 = polinomio(ys, x)
pol6 = polinomio(yi, x)

plot(x, pol5, "blue", x, pol6, "green", x, ys, "ro", x, yi, "ro")
grid("on")
show()






















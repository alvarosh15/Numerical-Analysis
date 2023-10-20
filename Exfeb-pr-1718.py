"""
Examen febrero 17/18 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import * 
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

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

""" Ejercicio 1 """

# Escribe una funcion que tenga como unico parametro de entrada x 
# y como unico parametro de salida p(x)

def polinomio(c):
    return eval_forma_newton_horner(x, y, c)

""" Ejercicio 2 """ 

# Dibuje la grafica de p en [0,2]

x = linspace(0, 2, 5)
y = array([1.533, 0.576, -0.554, -1.11, -2.1])
y2 = polinomio(x)
plot(x, y2, "b", x, 0*x, "black", x, y, "ro")
grid("on")
show()

""" Ejercicio 3 """

# Aplique el metodo de la secante para encontrar l, tomando 
# x0 = 0.5 x1 = 1 y test de parada 10^(-5)

def secante(f, x0, x1, eps, N):
    fx0=f(x0)
    fx1=f(x1)
    if fx0 ==0:
        print(an, 'es raíz de la función')
        return x0
    if fx1 == 0:
        print(bn, 'es raíz de la función')
        return x1
    error = eps +1 #siempre entra al bucle
    cont=0
    while (cont < N and error > eps):
       x2=x1 - (x1-x0)/(fx1-fx0)*fx1
       if isreal(f(x2)) == False:
           print('El punto no pertenece al dominio')
           return
       else:
        fx2=f(x2) 
        print('Iteración', cont, 'x2=', x2, 'f(x2)=', fx2)
        cont+=1
        error=abs(x2-x1)
        if fx2==0:
            return fx2
        x0=x1
        fx0=fx1
        x1=x2
        fx1=fx2
    print('La aproximación de la raíz en Regula Falsi tras', cont, 'iteraciones es', x2)
    if cont < N:
        print('Se ha alcanzado una aproximacion suficientemente proxima a', eps)
    else:
        print('Se ha alcanzado el número máximo de interaciones')
    
    return x2

secante(polinomio, 0.5, 1, 1e-5, 100)

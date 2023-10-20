"""
Practica 4 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import *
from matplotlib.pyplot import *

# Archivo pnewton.py

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

""" Ejercicio 1 """

""" Apartado A """

# Usar la funcion tabla_diferencias_divididas para calcular la tabla 
# de diferencias divididas asociadas a los datos 

x = linspace(0,1,5)
y = exp(x)
tabla_ejercicio1 = tabla_diferencias_divididas(x,y)
print(tabla_ejercicio1)

""" Ejercicio 2 """

""" Cálculo del polinomio de interpolación de Lagrange mediante la fórmula de Newton """

""" Apartado A """ 

# Usar la funcion de eval_forma_newton para evaluar los datos del 
# ejercicio 1 apartado A) en x = 1/3 y verificar que efectivamente
# el polinomio de interpolacion pasa por los datos dados en su definicion

x = linspace(0,1,5)
y = exp(x)
# print("El resultado de evaluar el polinomio en 1/3 es: " ,eval_forma_newton(x,y,1/3))
# print("El polinomio pasa por los puntos de evaluacion: " ,eval_forma_newton(x,y,x) == y)

""" Apartado B """ 

# Implementar un programa que evalua un polinomio en un punto z0 usando 
# el algoritmo de Horner 

def eval_pol_horner(p,z0):
    n = len(p)
    cn = p[n-1]
    for i in range (n-2,-1,-1):
        cn = p[i] + cn*z0
    return cn

# polinomio = array([-1,0,1])
# z0 = array([0,20])
# print(eval_pol_horner(polinomio,z0))

""" Apartado C """

# Modificar el algoritmo de horner

def eval_forma_newton_horner(x,y,z0):   
    n = len(y)
    df = tabla_diferencias_divididas(x,y)
    cn = df[n-1,n-1]
    for i in range (n-2,-1,-1):
        cn = cn*(z0-x[i])+df[i,i]
    return cn

x = linspace(0,1,5)
y = exp(x)
print("El resultado de evaluar el polinomio en 1/3 es: " ,eval_forma_newton_horner(x,y,1/3))
print("El polinomio pasa por los puntos de evaliacion: " ,eval_forma_newton_horner(x,y,x) == y)

""" Apartado D """

def apartado_d(f,a,b,N,z0):
    x = linspace(a,b,N+1)
    y = f(x)
    cn = eval_forma_newton_horner(x,y,z0)
    error = max(abs(f(z0) - cn))    
    return cn, error

""" Apartado E """

# Aplicar la función anterior a f(x) = e^x en el intervalo I = [−3,3], con 
# N = 5,10,15,20, siendo z0 el vector que resulta al dividir el 
# intervalo en porciones de longitud 0.01

z0 = linspace(-3,3,601)
for N in range (5,21,5):
    px, error = apartado_d(exp,-3,3,N,z0)
    plot(z0,exp(z0),"r",z0,px,"y")
    show()
    print("El error cometido con N =" ,N, "es" ,error)
            
""" Apartado F """

# Repetir el apartado anterior para f(x)=1/(1+x^2) en el intervalo I = [−5,5].

z0 = linspace(-5,5,1001)
def ff(x):
    return 1/(1 + x**2)
for N in range (5,21,5):
    px, error = apartado_d(ff,-5,5,N,z0)
    plot(z0,ff(z0),"r",z0,px,"y")
    show()
    print("El error cometido con N =" ,N, "es" ,error)

""" Apartado G """

# Analogo al apartado F 

""" Ejercicio 3 """

# El objetivo de este ejercicio es programar una funcion en python
# que dada una f: [a,b] -> R calcule la funcion lineal a trozos p
# que interpola los datos (x0, f(x0))...(xn,f(xn)) con nodos xk. 

""" Apartado A """

# Programar ambas funciones usando como parámetros de entrada la función f , 
# los extremos del intervalo [a, b] y el número de intervalos de la partición N. 
# Como parámetro de salida se asignará la handle del interpolante generado
# por la función interpd1.

def splineLin(f, a, b, N):
    x = linspace(a, b, N + 1)
    y = f(x)
    pol = inter1d(x, y, kind = "lineal")
    return pol

def splineCub(f, a, b, N):
    x = linspace(a, b, N + 1)
    y = f(x)
    pol = inter1d(x, y, kind = "cubic")
    return pol


























"""
Practica 5 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import quad

def funexp(x):
    return exp(-x**2)

iquad, equad =  quad(funexp,0,1)

""" Ejercicio 1 """

# Programar una funcion que implemente la regla del punto medio 

def puntomedio(f,a,b):
    c = 0.5*(a+b)
    ipuntomedio = (b-a)*f(c)
    epuntomedio = abs(ipuntomedio - iquad)
    print()
    print("La integral usando la Fórmula del Punto Medio es aproximadamente:",ipuntomedio, "y el 'error' es:",epuntomedio)
    return ipuntomedio

puntomedio(funexp,0,1)

""" Ejercicio 2 """

# Repetir el ejercicio 1 para la formula del trapecio 

def trapecio(f,a,b):
    itrapecio = 0.5*(b-a)*(f(a) + f(b))
    etrapecio= abs(itrapecio - iquad)
    print()
    print("La integral usando la Fórmula del Trapecio es aproximadamente:",itrapecio, "y el 'error' es:",etrapecio)
    return itrapecio

trapecio(funexp,0,1)

""" Ejercicio 3 """

# Repetir el ejercicio 1 para la formula de Simpson 

def simpson(f,a,b):
    c = 0.5*(a+b)
    isimpson = ((b-a)/6)*(f(a) + 4*f(c) + f(b))
    esimpson = abs(isimpson - iquad)
    print()
    print("La integral usando la Fórmula de Simpson es aproximadamente:",isimpson, "y el 'error' es:",esimpson)
    return isimpson

simpson(funexp,0,1)

""" Ejercicio 4 """

# Programar una funcion que implementa la regla del punto medio compuesta 

def puntomedioC(f,a,b,N):
    x = linspace(a,b,N+1)
    c = 0.5*(x[0:N] + x[1:N+1])
    integral = ((b-a)/N)*sum(f(c))
    error = abs(integral - iquad)
    print()
    print("[Fórmula del Punto Medio Compuesta] N = ",N,", h =",1/N,", Aproximación:",integral, ", 'Error':",error)
    return integral

puntomedioC(funexp,0,1,10)
puntomedioC(funexp,0,1,20)
puntomedioC(funexp,0,1,40)
puntomedioC(funexp,0,1,80)

""" Ejercicio 5 """

# Repetir el ejercicio anterior para la regla del trapecio compuesta

def trapecioC(f,a,b,N):
    x = linspace(a,b,N+1)
    integral = ((b-a)/(2*N))*(f(a) + f(b) + 2*sum(f(x[1:N])))
    error = abs(integral - iquad)
    print()
    print("[Fórmula del Trapecio Compuesta] N = ",N,", h =",1/N,", Aproximación:",integral, ", 'Error':",error)
    return integral

trapecioC(funexp,0,1,10)
trapecioC(funexp,0,1,20)
trapecioC(funexp,0,1,40)
trapecioC(funexp,0,1,80)

""" Ejercicio 6 """

# Repetir el ejercicio anterior para la regla de Simpson compuesta
 
def simpsonC(f,a,b,N):
    x = linspace(a,b,N+1)
    c = 0.5*(x[0:N] + x[1:N+1])
    fb = f(b)
    integral = ((b-a)/(6*N))*(f(a) + 2*sum(f(x[1:N])) + 4*sum(f(c) + fb))
    error = abs(integral - iquad)
    print()
    print("[Fórmula de Simpson Compuesta] N = ",N,", h =",1/N,", Aproximación:",integral, ", 'Error':",error)
    return integral

simpsonC(funexp,0,1,10)
simpsonC(funexp,0,1,20)
simpsonC(funexp,0,1,40)
simpsonC(funexp,0,1,80)

""" Ejercicio 7 """ 

# Programar una función que implemente la fórmula de Gauss de 3 puntos, 
# de nuevo con argumentos de entrada f , a y b, y de modo que, a partir 
# de los nodos y los pesos correspondientes a dicha fórmula en el intervalo 
# [−1,1], calcule los nodos y pesos correspondientes al intervalo [a,b],
# para posteriormente evaluar la expresión de la fórmula de cuadratura en ese 
# intervalo. Utilizarla para aproximar la integral del ejemplo y comparar el 
# valor obtenido con el ofrecido por quad.

def gauss3(f,a,b):
    t = array([-0.77459667,0,0.77459667])
    alphatilde = array([5/9, 8/9, 5/9])
    x = zeros(size(t))
    alpha = zeros(size(t))
    for k in range(size(t)):
        x[k] = a + 0.5*(b-a)*(t[k] + 1)
        alpha[k] = 0.5*(b-a)*alphatilde[k]
    gauss3 = sum(alpha*f(x))
    error = abs(gauss3 - iquad)
    print()
    print("[Fórmula de Gauss de 3 puntos] Aproximación:",gauss3,",'Error':",error)
    return gauss3

gauss3(funexp,0,1)










































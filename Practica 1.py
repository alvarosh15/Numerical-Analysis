"""
Practica 1 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import *
from matplotlib.pyplot import *

""" Ejercicio 1 """

# Funcion que devuelve la suma de a n veces

# Ejercicio hecho con bucle for

def sumanvecesfor(a,n):
    s = 0
    for k in range(n):
        s = s + a
    return s

# Ejercicio hecho con bucle while

def sumanveceswhile(a,n):
    s = 0
    contador = 0
    while(contador < n):
        s = s + a
        contador = contador + 1
    return s

""" Ejercicio 2 """

# Escribir un script que calcule la precisión de la máquina ε para los 
# números en coma flotante en Python, utilizando que ε= min {x∈F: 1+x>1}.

def precision(n):
    x = 1
    while(1 + x > 1):
        x = x/n
    print("El epsilon de la maquina es",x)
    
""" Ejercicio 3 """

# Representar gráficamente con Python la función f (x) = x − e^(−x)
# en el intervalo [−2, 2].

x = linspace(-2,2,500)
y =  x - exp(-x)
plot(x,y)
show()

""" Ejercicio 4 """

# Aproximación del número e como límite de una sucesión

# Aproxe toma como entrada n y devuelve la aproximación de e dada por
# (1 + 1/n)^n

def aproxe(n):
    return (1+1/n)**n

# Devuelve el valor absoluto cometido

def error(n):
    return exp(1) - aproxe(n)

""" Ejercicio 5 """

# Calcula la enesima suma parcial de la serie 1 / sqrt(k) con k incrementando
# hasta n 

def sumaparcial(n):
    s = 0
    for k in range(1,n+1):
        s = s + 1/sqrt(k)
    return s

""" Ejercicio 6 """

# Representa gráficamente los valores de Sn del problema anterior respecto a n

""" Ejercicio 7 """

# Calcula la enesima suma parcial de la serie 1 / (k*(k + 1))

def sumaparcial2(n):
    s = 0
    for k in range(1,n+1):
        s = s + 1/(k*(k+1))
    error  = abs(1-s)
    return s, error

# Calcular la suma parcial enesima anterior basada en la formula 
# 1 - 1/(n + 1)

def sumaparcial3(n):
    s = 1 - 1/(n+1)
    error = abs(1-s)
    return s, error

""" Ejercicio 8 """

# Aproximación del numero e según su serie de Taylor 

# Nos basamos en la igualdad e = exp(1) = Sumatorio(1 / k!)

# Devuelve el factorial de n

def factorial(n):
    s = 1
    for k in range (1,n+1):
        s = s*k
    return s

def etaylor(n):
    s = 1  # Sumamos ya para k = 0, porque al factorial que he programado es para n >= 1
    for k in range (1,n+1):
        s = s + 1/(factorial(k))
    return s

""" Ejercicio 9 """

# Aproximación de la función exp(x) mediante la serie de Taylor 

# Nos basamos en la igualdad exp(x) = Sumatorio(x^k / k!) 

# El programa toma un natural n y un real x y devuelve la aproximación de 
# e^x dada por la enesima suma parcial

def exptaylor(n,x):
    s = 1 # Sumamos ya para k = 0
    for k in range (1,n+1):
        s = s + (x**k)/(factorial(k))
    return s


""" Ejercicio 10 """

# Toma como entrada una lista y devuelve su suma, viene definida en Python 
# como sum del modulo numpy

def sumalista(lista):
    s = 0
    for k in range (0,len(lista)):
        s = s + lista[k]
    return s

# Toma como entrada una lista y devuelve su media, viene definida en Python
# como mean del modulo numpy

def medialista(lista):
    suma = sumalista(lista)
    media = suma/len(lista)
    return media



































"""
Examen 2021 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import *
from matplotlib.pyplot import *
from scipy.interpolate import interp1d
from scipy.integrate import quad

""" Ejercicio 1 """

def sumamedia(x): 
    suma = sum(x)
    media = suma / len(x)
    print("La media de ", x, " es ", media)
    return media

x = array([-1, -2, 0, 3, 2, 1])

print(sumamedia(x))

""" Ejercicio 2 """

def dicotomia(f,a,b,eps):
    print()
    print("----- MÉTODO DE DICOTOMÍA -----")
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    
    if (fan == 0):
        print (a, "es raíz de la función")
        return a
    elif (fbn == 0):
        print (b, "es raíz de la función")
        return b
    elif (fan * fbn > 0):
        print("No hay cambio de signo: no se puede aplicar el método")
        
    print("%1s %11s %11s" % ("k", "cn", "f(cn)" ))
    
    N = int((log(b-a) - log(eps))/log(2)) + 1
    
    for k in range(N):
        cn=(an+bn)/2.0
        fcn=f(cn)
        print("%1i %11.8f %11.8f" % (k, cn, fcn))
        if fcn==0:
            print("La raíz es:",cn)
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    return cn

def f(x):
    return sin(2*x)

dicotomia(f, 1, 2, 1e-8)

""" Ejercicio 3 """

def metodonewton(f,d,x0,eps,nmax):
    error = eps + 1
    k = 0
    print()
    print("----- METODO DE NEWTON -----")
    print("%2s %15s %15s" % ("k", "Xk", "|Xn - Xn-1|"))
    while (error > eps and k < nmax):
        x1 = x0 - f(x0)/d(x0)
        error = abs(x1 - x0)
        print("%2i %15.13f %15.13f" % (k, x1, error))
        x0 = x1
        k = k + 1
    print()
    print("La raiz es:",x1)
    return x1

def f3(x):
    return cos(0.5*x)

def d3(x):
    return -0.5*sin(0.5*x)

""" Ejercicio 4 """

x = linspace(-1,1,11)
y = [-0.0385, -0.0588, -0.1000, -0.2000, -0.5000 , -1.0000, -0.5000, -0.2000, - 0.1000, -0.0588, -0.0385]

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

def polinomio(c):
    return eval_forma_newton_horner(x, y, c)

def polinomioLineal(a, b):
    pol = interp1d(x, y, kind = "linear")
    return pol(x)

x2 = linspace(-1, 1, 100)

plot(x, y, "ro", x2, polinomio(x2), "r", x, polinomioLineal(-1, 1), "b")
show()

""" Ejercicio 5 """

def trapeciocomp(x,y):
    N = len(y)
    a = x[0]
    b =x[N - 1]
    integral = ((b-a)/(2*N))*(y[0] + y[N-1] + 2*sum((y[1:N-2])))
    print()
    print("[Fórmula del Trapecio Compuesta] La integral es aproximadamente:",integral)
    return integral

trapeciocomp(x,y)

print()
print("El resultado obtenido es el valor aproximado de la integral de polinomioInt (el polinomio de interpolacion) del Ejercicio 4")














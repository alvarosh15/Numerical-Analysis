"""
Practica 2 con comentarios

Álvaro Sánchez Hernández
"""

from numpy import *
from matplotlib.pyplot import *

""" Ejercicio 1 """

""" Apartado A """

# Aplicamos el método de dicotomía 

def dicotomia(f,a,b,N):
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
    for k in range(N):
        cn=(an+bn)/2.0
        fcn=f(cn)
        print("%1i %11.8f %11.8f" % (k, cn, fcn))
        if fcn==0:
            print(cn, "es la raíz de la función")
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print("La aproximacion de la raíz tras",N, "iteraciones es",cn)
    print()
    return cn

""" Apartado B """

# Aplicar el método de dicotomía a x^5 - 5x^3 + 1 para aproximar la solución
# en [0,1] con 20 iteraciones 

def funcion1(x):
    return x**5 - 5*(x**3) + 1

# Mostramos la gracia de la función

# x = linspace(-3,3,100)
# y = funcion1(x)

# plot(x,y,"r",x,0*x)
# xlabel("Eje X")
# ylabel("Eje Y")
# show()

# Aplicamos el metodo de dicotomía en [0,1] con 20 iteraciones 

# dicotomia(funcion1,0,1,20)

""" Apartado C """

# Aplicar el método de dicotomía a cos(x) - x para aproximar la solución
# en [un intervalo correcto con 20 iteraciones 

def funcion2(x):
    return cos(x) - x

    
# x2 = linspace(0,2*pi,100)
# y2 = funcion2(x2)

# plot(x2,y2,"r",x2,0*x2)
# xlabel("Eje X")
# ylabel("Eje Y")
# show()

""" Apartado D """

# Modificar dicotomia para que los parametros de entrada sean:
# La funcion f a la que se le busca el cero
# Los extremos a y b del intervalo que contiene a ese cero
# La precisión epsilon con la que se desea aproximar el cero

# El programa calcula el numero de iteraciones necesarias usando la 
# expresion de N que podemos ver abajo

def dicotomia2(f,a,b,eps):
    print()
    print("----- MÉTODO DE BISECCIÓN -----")
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

""" Apartado E """

# Aplicar el metodo anterior para aproximar las funciones anteriores
# con un error menor que 10^(-7)

# dicotomia2(funcion2,0,1,10e-7)

""" Ejercicio 2 """

# Aplicar el metodo de regula falsi

""" Apartado A """

# Los parametros de entrada son:
# La funcion f a la que se le busca el cero
# Los extremos a y b del intervalo al que se le busca el cero
# La precision epsilon con la que se desea aproximar el cero
# El numero max de iteraciones 

def regulafalsi(f,a0,b0,eps,N):
    print()
    print("----- MÉTODO DE REGULA-FALSI -----")
    print("%1s %13s %13s" % ("k", "ck", "f(ck)"))
    an = a0
    bn = b0
    fan = f(an)
    fbn = f(bn)
    ck = 0
    
    if fan == fbn:
        return "Error: f(ak) = f(bk)"    
    for k in range(N):
        cn = bn - (bn - an)*fbn/(fbn - fan)
        fcn = f(cn)
        print("%1i %13.10f %13.10f" % (k, cn, fcn))
        if fcn==0:
            print("La raíz es:",cn)
            return cn
        elif abs(cn - an) <= eps:
            print("%1i %13.10f %13.10f" % (k, cn, fcn))
            print("Hemos alcanzado una aproximación saitsfactoria")
            return cn
        elif abs(cn - bn) <= eps:
            print("%1i %13.10f %13.10f" % (k, cn, fcn))
            print("Hemos alcanzado una aproximación saitsfactoria")
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print("Se han tenido que hacer las",N ,"iteraciones")
    return cn

""" Apartado B """

# Aplicar la funcion regulafalsi a las mismas ecuaciones del ejercicio 1
# con cota de error 10^(-7)

# regulafalsi(funcion1,0,1,10e-7,100)
# regulafalsi(funcion1,-3,-2,10e-7,100)
# regulafalsi(funcion1,2,3,10e-7,100)       
# regulafalsi(funcion2,0,1,10e-7,100)

""" Apartado C """

# Modificar el programa para que el algoritmo pare cuando se llegue a 
# una aproximaciíon en la que se tenga que abs(f(cn)) <= Epsilon

def regulafalsi2(f,a0,b0,eps,N):
    print()
    print("----- MÉTODO DE REGULA-FALSI -----")
    print("%1s %13s %13s" % ("k", "ck", "f(ck)"))
    an = a0
    bn = b0
    fan = f(an)
    fbn = f(bn)
    ck = 0
    
    if fan == fbn:
        return "Error: f(ak) = f(bk)"
    
    for k in range(N):
        cn = bn - (bn - an)*fbn/(fbn - fan)
        fcn = f(cn)
        print("%1i %13.10f %13.10f" % (k, cn, fcn))
        if fcn==0:
            print("La raíz es:",cn)
            return cn
        elif abs(fcn) <= eps:
            print("%1i %13.10f %13.10f" % (k, cn, fcn))
            print("Hemos alcanzado una aproximación saitsfactoria")
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    print("Se han tenido que hacer las",N ,"iteraciones")
    return cn


""" Apartado D """

# Aplicar la funcion regulafalsi2 a las mismas ecuaciones del ejercicio 1
# con cota de error 10^(-7)

# regulafalsi2(funcion1,0,1,1e-7,20)
# regulafalsi2(funcion1,-3,-2,1e-7,20)
# regulafalsi2(funcion1,2,3,e-7,20)       
# regulafalsi2(funcion2,0,1,1e-7,20)


""" Ejercicio 3 """

# Aplicar el metodo de la secante 

""" Apartado A """


# Los parametros de entrada son:
# La funcion f a la que se le busca el cero
# Las aproximaciones iniciales x0 y x1
# La precision epsilon con la que se desea aproximar el cero
# El numero maximo de iteraciones 

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

""" Apartado B """

# Aplicar el metodo de la secante a las funciones del ejercicio 1
# con un error de 10^(-7) 

# secante(funcion1, 0, 1, 1e-7, 20)

""" Apartado C """ 

# Modificarlo para que se detenga si abs(f(xn)) <= Epsilon 

def secante2(f,a,b,x0,x1,eps):  
    print()
    print("----- MÉTODO DE LAS SECANTES -----")
    print("%1s %13s %13s" % ("k", "xk", "f(xk)"))
    def secante2(f,a,b,x0,x1,eps,k):
        if f(x0) == f(x1):
            return "Error: f(x0) = f(x1)"
        else:
            x2 = x1 - (x1 - x0)*f(x1)/(f(x1) - f(x0))
            if x2 >= a:
                if x2 <= b:
                    if f(x2) == 0:
                        print("La raiz es:" ,x2)
                    else:
                        if abs(f(x2)) <= eps:
                            print("%1i %13.10f %13.10f" % (k, x2, f(x2)))
                            return x2
                        else:
                            print("%1i %13.10f %13.10f" % (k, x2, f(x2)))
                            secante2(f,a,b,x1,x2,eps,k+1)
    return secante2(f,a,b,x0,x1,eps,0) 

""" Apartado D """

# Analogo al apartado B pero con secante2 

# secante2(funcion1, 0, 1, 1e-7, 20)





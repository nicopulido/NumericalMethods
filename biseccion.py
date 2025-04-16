from sympy import symbols, Eq,sin, cos,log,exp, lambdify
import math
from decimal import Decimal

x = symbols('x')



inputFuncion = input("Ingrese una ecuación: ")
errorDeseado = float(input("Ingrese el error: "))
xl = int(input("Ingrese el limite inferior del intervalo: "))

xu = int(input("Ingrese el limite superior del intervalo: "))

parte_izq = eval(inputFuncion.split('=')[0])
parte_der = eval(inputFuncion.split('=')[1])

funcion = lambdify(x,parte_izq - parte_der)

#en función "igualo a 0" y creo una función a partir de eso
#el .split lo que hace es dividir la cadena donde está el igual [0] y [1] es para dividir la parte izquierda y derecha respectivamente
#eval() evalua la cadena como expresion para Sympy
#Eq() toma argumentos de izquierda y derecha para construir una relación de igualdad

ErrAbsMaximo = math.ceil(1/math.log(2) * math.log((xu - xl)/errorDeseado))

errorRelAproxPorcentual = math.fabs((xu - xl)/(xu + xl))*100

n = -1

print("\nDebe hacerse como máximo con n: " + str(ErrAbsMaximo))

print(f"{'n':<4}{'Xl':<30}{'Xu':<30}{'f(Xl)':<30}{'f(Xu)':<30}{'Xr':<30}{'f(Xr)':<30}")


# and (ErrAbsMaximo > n) esto es por si toca tener cota superior

while((errorRelAproxPorcentual > errorDeseado)):
    n+=1
    funcionXl = funcion(xl)
    funcionXu = funcion(xu)
    xr = (xl + xu)/2
    funcionXr = funcion(xr)
    
    print(f"{n:<4}{xl:<30}{xu:<30}{funcionXl:<30}{funcionXu:<30}{xr:<30}{funcionXr:<30}")
    
    if(funcionXr*funcionXl < 0):
        xu = xr
    else:
        xl = xr
    
    errorRelAproxPorcentual = math.fabs((xu - xl)/(xu + xl))*100


print("\nLa raíz es:" + str(Decimal(xr)))
print("Con error relativo aproximado porcentual: " + str(errorRelAproxPorcentual))
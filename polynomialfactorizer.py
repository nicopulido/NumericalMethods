from sympy import symbols, Eq,sin, cos,log,exp,diff, Poly, lambdify
import math

def sinteticDivision(polinomial, x, Xn):
    derivatedFunction = diff(polinomial(x), x)
    Xn_1 = Xn - polinomial(Xn)/derivatedFunction(Xn)
    while(derivatedFunction(Xn_1) != 0):
        Xn = Xn_1
        Xn_1 = Xn - polinomial(Xn)/derivatedFunction(Xn)
    return Xn_1

def reducePolinomial(polinomial, x, Xn):
    derivatedFunction = diff(polinomial(x), x)







x = symbols('x')

polinomial = lambdify(Poly(x, input("Ingrese una función: ")))
givenError = float(input("Ingrese el error esperado: "))


print(Poly(polinomial(x), x).all_coeffs())

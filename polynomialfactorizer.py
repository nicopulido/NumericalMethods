from sympy import symbols, Poly 
import math



def sinteticDivision(polynomial, x, Xn):
    derivatedPoly = polynomial.diff(x)
    Xn = Xn - polynomial.subs(x, Xn)/derivatedPoly.subs(x, Xn)
    while(derivatedPoly(Xn) != 0):
        Xn = Xn - polynomial.subs(x, Xn)/derivatedPoly.subs(x, Xn)
    return Xn

def reducePolynomial(polyCoefficients, Xn):
    reducedPolynomial = [polyCoefficients[0]]
    for i in range(1, len(polyCoefficients) - 1):
        reducedPolynomial.append(reducedPolynomial[-1] * Xn + polyCoefficients[i])
    return reducedPolynomial

x = symbols('x')

polynomial = Poly(input("Ingrese el polinomio: "), x)

while(not polynomial.is_irreducible):
    Xn = sinteticDivision(polynomial, x, 0)

    polyCoefficients = polynomial.all_coeffs()
    reducedPolynomial = reducePolynomial(polyCoefficients, x, Xn)

    polynomial = Poly(reducedPolynomial, x)

print(polynomial.as_expr())
    
      





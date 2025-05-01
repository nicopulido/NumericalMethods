from sympy import symbols, Poly, Rational
from math import gcd
from functools import reduce

##function to sinthetic division
# this function is used to find the roots of the polynomial using sinthetic division

def sinteticDivision(polynomial, x,):
    derivatedPoly = polynomial.diff(x)

    for i in range(1, 101):
        for Xn in [i, -i]:  
            while abs(polynomial.subs(x, Xn)) > 1e-20:
                Xn = Xn - polynomial.subs(x, Xn) / derivatedPoly.subs(x, Xn)

            
            if(polynomial.subs(x, int(round(Xn))) == 0):
                return Xn
    

            if(polynomial.subs(x,Rational(Xn).limit_denominator()) == 0):
                return Rational(Xn).limit_denominator()

#function to normalize coefficients
# this function is used to normalize the coefficients of the polynomial to make them integers

def normalize_coefficients(coefficients):
    gcd_value = reduce(gcd, [int(c) for c in coefficients if c != 0])
    return [c / gcd_value for c in coefficients]

#function to reduce polynomial
# this function is used to reduce the polynomial after sinthetic division

def reducePolynomial(polyCoefficients, Xn):
    reducedPolynomial = [polyCoefficients[0]]
    for i in range(1, len(polyCoefficients) - 1):
        reducedPolynomial.append(reducedPolynomial[-1] * Xn + polyCoefficients[i])
    return normalize_coefficients(reducedPolynomial)

#function to factorize polynomials
# this function is used to factorize the polynomial using sinthetic division and reducePolynomial functions

def factorizePolynomials(polynomial, x):
    while not polynomial.is_irreducible:

        Xn = sinteticDivision(polynomial, x)

        if abs(Xn - round(Xn)) < 1e-10:
            Xn = int(round(Xn))

        if Xn == 0:
            print("x", end="")
        elif Xn > 0:
            print("(" + "x - " + str(Rational(Xn).limit_denominator()) + ")", end="")
        else:
            print("(" + "x + " + str(Rational(-Xn).limit_denominator()) + ")", end="")

        polyCoefficients = polynomial.all_coeffs()

        reducedPolynomial = reducePolynomial(polyCoefficients, Xn)

        leading_coefficient = reducedPolynomial[0]
        reducedPolynomial = [c / leading_coefficient for c in reducedPolynomial]

        reducedPolynomial = [
            int(c) if abs(c - round(c)) < 1e-20 else c for c in reducedPolynomial
        ]

        polynomial = Poly(reducedPolynomial, x)

    if polynomial.degree() == 1 and polynomial.all_coeffs()[0] != 1:
        coeffs = polynomial.all_coeffs()
        a = coeffs[0]
        b = coeffs[1]
        root = -b / a
        print(f"(x - {Rational(root).limit_denominator()})")
    else:
        print("(" + str(polynomial.as_expr()) + ")")


x = symbols('x')
polynomial = Poly(input("Ingrese un polinomio: "), x)
factorizePolynomials(polynomial, x)

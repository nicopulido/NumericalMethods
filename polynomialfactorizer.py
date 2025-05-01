from sympy import symbols, Poly 
import math



def sinteticDivision(polynomial, x,):
    derivatedPoly = polynomial.diff(x)

    # Iterate over possible values for Xn from 1 to 100 and their negatives
    for i in range(1, 101):
        for Xn in [i, -i]:  # Test both positive and negative values  # Check if Xn is a root     # Use the while loop to refine the root                print(Xn)
            while abs(polynomial.subs(x, Xn)) > 1e-10:
                print("Xn evaluado en el polinomio: " + str(round(polynomial.subs(x, Xn), 5)))
                print(round(Xn, 5))
                Xn = Xn - polynomial.subs(x, Xn) / derivatedPoly.subs(x, Xn)
            return Xn 

def reducePolynomial(polyCoefficients, Xn):
    reducedPolynomial = [polyCoefficients[0]]
    for i in range(1, len(polyCoefficients) - 1):
        reducedPolynomial.append(reducedPolynomial[-1] * Xn + polyCoefficients[i])
    return reducedPolynomial


x = symbols('x')

polynomial = Poly(input("Ingrese el polinomio: "), x)

while(not polynomial.is_irreducible):

    Xn = sinteticDivision(polynomial, x)

    if(Xn == 0):
        print("x", end="")
    elif(Xn > 0):
        print("(" + "x - " +  str(round(Xn, 5)) + ")", end="")
    else:
        print("(" + "x + " +  str(round(-Xn, 5))  + ")", end="")

    polyCoefficients = polynomial.all_coeffs()
    reducedPolynomial = reducePolynomial(polyCoefficients, Xn)

    polynomial = Poly(reducedPolynomial, x)
    
print("(" + str(polynomial.as_expr().evalf(5)) + ")")
    
      





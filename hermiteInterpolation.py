#this will be a file where the input will be 3 x, 3 f(x), 3 f'(x)
#and the output will be the hermite polynomial
# the hermite polynomial will be of the form 2n+1
# n being the number of points

import numpy as np
import sympy
from sympy import symbols, Poly, lambdify
import matplotlib.pyplot as plt

def findPartialLagrangePoly(X_kpoints, x):
    """
    Evaluate the derivative of the Lagrange polynomial at a given point x.
    """
    n = len(X_kpoints)
    polynomial = Poly(1, x)
    results = []

    for i in range(n):
        xi = X_kpoints[i]
        for j in range(n):
            if i != j:
                xj = X_kpoints[j]
                polynomial *= (x - xj) / (xi - xj)
        results.append(polynomial)
        polynomial = Poly(1, x)
    return results

def eval_partial_lagrange_derivate(parcialLagrangePoly, X_kpoints, x):
    """
    Evaluate the derivative of the Lagrange polynomial at a given point x.
    """
    results = []
    for i in range(len(parcialLagrangePoly)):
        results.append(parcialLagrangePoly[i].diff(x).eval(X_kpoints[i]))
    return results

def find_hermite_polynomial(X_kpoints, fpoints, dfpoints, n, x):
    """
    Find the Hermite polynomial using the given points and their derivatives.
    """

    partialLagrangePoly = findPartialLagrangePoly(X_kpoints, x)

    partialHermitePolys = []
    partialHermiteHatPolys = []

    for i in range(n):
        xi = X_kpoints[i]
        fi = fpoints[i]
        dfi = dfpoints[i]

        # Calculate the Hermite polynomial
        H_i = (1 - 2 * (x - xi) * partialLagrangePoly[i].diff(x).eval(xi)) * partialLagrangePoly[i]**2

        # Calculate the Hermite hat polynomial
        H_hat_i = (x - xi) * partialLagrangePoly[i]**2

        partialHermitePolys.append(H_i * fi)
        partialHermiteHatPolys.append(H_hat_i * dfi)
    # Sum the Hermite polynomials and the Hermite hat polynomials       
        

    return sum(partialHermitePolys) + sum(partialHermiteHatPolys)


def drawFunction(hermitePoly, symbol, points, yvalues):
    hermiteFunc = sympy.lambdify(symbol, hermitePoly.as_expr(), "numpy")
    X = np.linspace(points[0],points[-1])
    Y = hermiteFunc(X)
    plt.scatter(points, yvalues, color = "orange")
    if len(points) == 2:
        plt.plot(X, Y, label="Hermite Polynomial from: " + str(points))  
        plt.xlabel("x")
        plt.ylabel("y")
    else:
        plt.plot(X, Y, label="Hermite Polynomial from: " + str(hermitePoly.as_expr()))
        plt.xlabel("x")
        plt.ylabel("y")

    
# Example usage:
points = []
yvalues = []
dfvalues = []
x = symbols('x')

numberOfPoints = int(input("Enter the number of points: "))
for i in range(numberOfPoints):
    point = float(input(f"Enter the X_k value for point {i+1}: "))
    fValue = float(input(f"Enter the f({point}) value for point {i+1}: "))
    dfValue = float(input(f"Enter the f'({point}) value for point {i+1}: "))
    points.append(point)
    yvalues.append(fValue)
    dfvalues.append(dfValue)

for i in range(numberOfPoints - 1):
    hermitePol = find_hermite_polynomial(points[i: i + 2], yvalues[i: i + 2], dfvalues[i: i + 2], 2, x)
    drawFunction(hermitePol, x, points[i:i + 2], yvalues[i:i + 2])
    
hermitePoly = find_hermite_polynomial(points, yvalues, dfvalues, numberOfPoints, x)
drawFunction(hermitePoly, x, points, yvalues)

plt.title("Hermite Interpolating Polynomial")
plt.legend()
plt.grid(True)

plt.show()


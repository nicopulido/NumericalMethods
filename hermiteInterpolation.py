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


def drawCubicSplines(hermitePoly, symbol, points, yvalues):
    hermiteFunc = sympy.lambdify(symbol, hermitePoly.as_expr(), "numpy")
    X = np.linspace(points[0],points[-1])
    Y = hermiteFunc(X)
    plt.scatter(points, yvalues, color = "orange")
    plt.plot(X, Y, label="Hermite Polynomial")

    


X_kpoints = []
fpoints = []
dfpoints = []
x, y= symbols('x y')


X_kpoints.append(-2)
X_kpoints.append(1)

fpoints.append(-12)
fpoints.append(9)

dfpoints.append(22)
dfpoints.append(10)


print(find_hermite_polynomial(X_kpoints, fpoints, dfpoints, len(X_kpoints), x))
print(type(find_hermite_polynomial(X_kpoints, fpoints, dfpoints, len(X_kpoints), x)))

# To write a Poly type as a function and plot it on an x, y graph:
hermite_poly = find_hermite_polynomial(X_kpoints, fpoints, dfpoints, len(X_kpoints), x)


drawCubicSplines(hermite_poly,x,X_kpoints,fpoints)

plt.show()


"""points = []

for i in range(1):
    x = symbols('x')
    X_k = float(input("Enter the X_k value: "))
    f = float(input("Enter the f(" + str(X_k) + ") value: "))
    df = float(input("Enter the f'(" + str( X_k )+ ") value: "))
    points.append((X_k, f, df))

X_kpoints = []
fpoints = []
dfpoints = []
x, y= symbols('x y')


X_kpoints.append(-2)
X_kpoints.append(1)

fpoints.append(-12)
fpoints.append(9)

dfpoints.append(22)
dfpoints.append(10)


print(find_hermite_polynomial(X_kpoints, fpoints, dfpoints, len(X_kpoints), x))
print(type(find_hermite_polynomial(X_kpoints, fpoints, dfpoints, len(X_kpoints), x)))

# To write a Poly type as a function and plot it on an x, y graph:
hermite_poly = find_hermite_polynomial(X_kpoints, fpoints, dfpoints, len(X_kpoints), x)
hermite_func = sympy.lambdify(x, hermite_poly.as_expr(), "numpy")
X = np.linspace(-2, 1, 400)
Y = hermite_func(X)

plt.scatter(X_kpoints,fpoints,label = "Interpolation Points", color = "orange")
plt.plot(X, Y, label="Hermite Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Hermite Interpolating Polynomial")
plt.legend()
plt.grid(True)
plt.show()
"""
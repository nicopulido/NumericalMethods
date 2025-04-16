from sympy import symbols, Eq, lambdify
import math
import cmath

x = symbols('x')

function = lambdify(x, input())

givenError = float(input())

x_0 = float(input())
x_1 = float(input())
x_2 = float(input())

#given the supossition that x_0 is the min valor and x_2 the max valor

givenError = math.ceil((1/math.log(2)) * math.log((x_2 - x_0)/givenError))

print(f"{'n':<5}{'X0':<5}{'X1':<5}{'X2':<5}{'h0':<5}{'h1':<5}{'f(x0)':<5}{'f(x1)':<5}{'f(x2)':<5}{'d0':<5}{'d1':<5}{'a':<5}{'b':<5}{'c':<5}{'X3':<5}")

for i in range (givenError):
    h_0 = x_1 - x_0
    h_1 = x_2 - x_1
    d_0 = (function(x_1) - function(x_0))/(x_1 - x_0)
    d_1 = (function(x_2) - function(x_1))/(x_2 - x_1)
    a = (d_1 - d_0)/(h_0 + h_1)
    b = a * h_1 + d_1
    c = function(x_2)

    
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    if abs(discriminant + b) < abs(discriminant - b):
        discriminant = - discriminant
    
    x_3 = (-2 * c)/(b + discriminant)

    print(f"{(i+1):<5}{x_0:<5.5f}{x_1:<5.5f}{x_2:<5.5f}{h_0:<5.5f}{h_1:<5.5f}{function(x_0):<5.5f}{function(x_1):<5.5f}{function(x_2):<5.5f}{d_0:<5.5f}{d_1:<5.5f}{a:<5.5f}{b:<5.5f}{c:<5.5f}{x_3:<5.5f}")

    x_0 = x_1
    x_1 = x_2
    x_2 = x_3


    
from sympy import symbols, Eq, lambdify
import math
import cmath

def complexFunction(function, x_0, x_1, x_2, givenError):

    givenError = math.ceil((1/math.log(2)) * math.log((x_2 - x_0)/givenError))

    print(f"{'n':<10}{'X0':<10}{'X1':<10}{'X2':<10}{'h0':<10}{'h1':<10}{'f(x0)':<10}{'f(x1)':<10}{'f(x2)':<10}{'d0':<10}{'d1':<10}{'a':<10}{'b':<10}{'c':<10}{'X3':<10}")

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

        print(f"{(i+1):<10}{x_0:<10.5f}{x_1:<10.5f}{x_2:<10.5f}{h_0:<10.5f}{h_1:<10.5f}{function(x_0):<10.5f}{function(x_1):<10.5f}{function(x_2):<10.5f}{d_0:<10.5f}{d_1:<10.5f}{a:<10.5f}{b:<10.5f}{c:<10.5f}{x_3:<10.5f}")

        x_0 = x_1
        x_1 = x_2
        x_2 = x_3

def realFunction(function, x_0, x_1, x_2, givenError):

    print(f"{'n':<10}{'X0':<10}{'X1':<10}{'X2':<10}{'h0':<10}{'h1':<10}{'f(x0)':<10}{'f(x1)':<10}{'f(x2)':<10}{'d0':<10}{'d1':<10}{'a':<10}{'b':<10}{'c':<10}{'X3':<10}")

    h_0 = x_1 - x_0
    h_1 = x_2 - x_1
    d_0 = (function(x_1) - function(x_0))/(x_1 - x_0)
    d_1 = (function(x_2) - function(x_1))/(x_2 - x_1)
    a = (d_1 - d_0)/(h_0 + h_1)
    b = a * h_1 + d_1
    c = function(x_2)
    i = 0

    givenError = math.ceil((1/math.log(2)) * math.log((x_2 - x_0)/givenError))

    while((b**2 > 4*a*c) and (i < givenError)):
        i += 1

        discriminant = math.sqrt(b**2 - 4*a*c)

        if abs(discriminant + b) < abs(discriminant - b):
            discriminant = - discriminant

        x_3 = (-2 * c)/(b + discriminant)

        print(f"{(i+1):<10}{x_0:<10.5f}{x_1:<10.5f}{x_2:<10.5f}{h_0:<10.5f}{h_1:<10.5f}{function(x_0):<10.5f}{function(x_1):<10.5f}{function(x_2):<10.5f}{d_0:<10.5f}{d_1:<10.5f}{a:<10.5f}{b:<10.5f}{c:<10.5f}{x_3:<10.5f}")

        x_0 = x_1
        x_1 = x_2
        x_2 = x_3

        h_0 = x_1 - x_0
        h_1 = x_2 - x_1
        d_0 = (function(x_1) - function(x_0))/(x_1 - x_0)
        d_1 = (function(x_2) - function(x_1))/(x_2 - x_1)
        a = (d_1 - d_0)/(h_0 + h_1)
        b = a * h_1 + d_1
        c = function(x_2)



x = symbols('x')

function = lambdify(x, input())

givenError = float(input())

x_0 = float(input())
x_1 = float(input())
x_2 = float(input())

#given the supossition that x_0 is the min valor and x_2 the max valor

realFunction(function, x_0, x_1, x_2, givenError)


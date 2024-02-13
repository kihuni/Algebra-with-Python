
# Problem 1
"""
# Importing necessary libraries
import sympy
from sympy import symbols
from sympy.solvers import solve

# Problem 1

# Defining the symbol
X = symbols('X')

# Defining the equation
eq = 4*X**2 - 4*X - 3

# Solving the equation
sol = solve(eq, X)

# Printing the solution
print(sol)
"""

# Problem 2
# prompt for someone to enter the equation

"""
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
eq = input("Enter the equation: ")

print("The solution is: ", solve(eq, x))
"""
# Problem 3
# Multiple solutions

"""
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
eq = input("Enter the equation: ")

solutions = solve(eq, x)
for solution in solutions:
    print("The solution is: ", solution)
"""

"""
from sympy import *

var('x y')

first = 2*x + 10

# Sympy syntax for equation equal to zero, ready to factor
eq1 = Eq(first, y)

# sympy solve for x
sol = solve(eq1, x)

# show solution

print("x = ", sol[0])
"""

import sympy 
from sympy import symbols


var('x y')

# Equation set equal to zero, ready to factor
eq = 2*x + 10*y + 4

sympy.factor(eq)


# Explaining how each functions works

# converting string input(including fractions) to float

def string_frac(in_string):
    if '/' in in_string:
        nd = in_string.split('/')
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
    else:
        return float(in_string)
    
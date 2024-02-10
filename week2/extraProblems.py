
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

import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
eq = input("Enter the equation: ")

solutions = solve(eq, x)
for solution in solutions:
    print("The solution is: ", solution)
    
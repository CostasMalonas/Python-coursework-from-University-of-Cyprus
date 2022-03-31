import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve
from scipy.optimize import fsolve

#SOURCE: https://stackoverflow.com/questions/22742951/solve-an-equation-using-a-python-numerical-solver-in-numpy
#coeff_1 = [1, 5, 2]
#print(np.roots(coeff_1))

#coeff_2 = [1, 2, -6, 2]
#print(np.roots(coeff_2))

# FIRST EQUATION
# It returns a figure and an axes element. Figure holds all plot elements, axes contains most of the figure elements
fig, ax = plt.subplots() 

func_1 = lambda x : x**2 + 5*x + 2 # We define the expression whose roots we want to find

x = np.linspace(-5, 4, 100) # Return evenly spaced numbers over a specified interval. https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
#print('x is ', x)
ax.plot(x, func_1(x)) # Plot x numpy array at x axis and the result of the func1 at the y axis
ax.set_xlabel("x first equation") # Set x axis label
ax.set_ylabel("expression value first equation") # Set y axis label
ax.grid() # Add grid
plt.show() # Show the plot

# We need a good initial guess for fsolve(). Thanks to our plot we can see where our
# function is becoming 0
x_initial_guess = [-4, -0.5] 
eq_1_solution = fsolve(func_1, x_initial_guess) # We pass our function and our initial guesses

print(eq_1_solution) # Print the roots



# SECOND EQUATION
fig_2, ax_2 = plt.subplots() # We create another figure

func_2 = lambda x: x**3 + 2*x**2 - 6*x + 2 # We create our equation

x = np.linspace(-4, 3, 400) # Return evenly spaced numbers over a specified interval. https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
#print('x is ', x)
ax_2.plot(x, func_2(x)) # Plot x numpy array at x axis and the result of the func1 at the y axis
ax_2.set_xlabel("x second equation") # Set x axis label 
ax_2.set_ylabel("expression value second equation") # Set y axis label
ax_2.grid() # Add grid
plt.show() # Show the plot

x2_initial_guess = [-3.74482608, 0.39593186,  1.34889422] # List with initial guesses

eq_2_solution = fsolve(func_2, x2_initial_guess)

print(eq_2_solution) # Print roots
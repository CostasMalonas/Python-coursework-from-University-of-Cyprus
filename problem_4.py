
# (i)

from random import  uniform


"""


n = 1000 -> Wall time: 1 ms
n = 10000 -> Wall time: 6 ms
n = 100000 -> Wall time: 58 ms
n = 1000000 -> Wall time: 615 ms
n = 10000000 -> Wall time: 6.35 s


"""

def average_py(n):
    """
    This function takes an integer n as parameter.
    We declare an empty list called num_list where
    we will store our random numbers. Inside the for loop
    for n times we take a uniform distributed number from the
    interval (0,1) and we append it to the num_list.
    At the end we return the average

    """
    num_list = []
    for r in range(n):
        num = uniform(0, 1) #  the probability of getting 0 or 1 is zero.
        num_list.append(num)
    return sum(num_list)/n


average_py(1000000)







# (ii)
"""
n = 1000 -> Wall time: 0 ns
n = 10000 -> Wall time: 5 ms
n = 100000 -> Wall time: 49 ms
n = 1000000 -> Wall time: 528 ms
n = 10000000 -> Wall time: 5.28 s

    

"""
# Here we use n == 1000. 
sum([uniform(0,1) for num in range(1000)])/1000





# (iii)

import numpy as np

"""
At the following function we pass n uniform distributed numbers in the 
interval (0,1). To do that we import the numpy library and call 
the uniform method.
We store those numbers inside the num_list and we return the average


EXECUTION WITH %time
We executed the function for n from 1000 to 10000000

n = 1000 -> Wall time: 0 ns
n = 10000 -> Wall time: 15.6 ms
n = 100000 -> Wall time: 31.2 ms
n = 1000000 -> Wall time: 250 ms
n = 10000000 -> Wall time: 2.34 s


"""

def average_np(n): # n uniform distributed nubers in the interval (0,1)
    num_list = [] # We declare the list of the random numbers
    num_list = np.random.uniform(0,1, n) # We take the n random numbers
    return sum(num_list)/n # We compute the average
    



average_np(1000)




# (iv)





from random import  uniform
from numba import jit

"""
The following function is the same with the average_py only now with
Numba our runtime was higly improved. We only needed to apply
the @jit decorator to our function and now we can give n values
that without Numba our function wouldn't terminate.

We tried for n = 10000 to 100000000 

n = 10000 -> Wall time: 0 ns
n = 100000 -> Wall time: 78 ms
n = 1000000 -> Wall time: 796 ms
n = 10000000 -> Wall time: 7.96 s
n = 100000000 -> Wall time: 1min 21s
"""
@jit
def average_nb(n):
    num_list = []
    for r in range(n):
        num = uniform(0, 1) #  the probability of getting 0 or 1 is zero.
        num_list.append(num)
    return sum(num_list)/n


average_nb(100000)



"""
The least execution time has it the numpy method(average_np) with 2.34s for n = 10million

  The following order represents time from lower to bigger
 (iii) < (ii) < (i) < (iv)


"""








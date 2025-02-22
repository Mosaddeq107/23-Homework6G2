import numpy as np
import matplotlib.pyplot as plt

def simpson(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite Simpson's rule, using n subintervals.
    From http://en.wikipedia.org/wiki/Simpson's_rule
    """

    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")

    h = (b - a) / n
    i = np.arange(0,n)

    s = f(a) + f(b)
    s += 4 * np.sum( f( a + i[1::2] * h ) )
    s += 2 * np.sum( f( a + i[2:-1:2] * h ) )



    return s * h / 3


def cumulative_integral_simpson(f,a,b,dx):
    """Function that calculates the antidervative of f"""

    x_values = np.arange(a,b,dx)

    num_of_steps = np.floor((b-a)/dx)

    if num_of_steps < 2:
        raise ValueError("(b-a)/dx  must be at least 2")

    antiderivative = np.empty(len(x_values)+1)

    antiderivative[0] = simpson(f, a, a+dx, 4)

    j = 1

    while j <= num_of_steps :

      antiderivative[j] = antiderivative[j-1] + simpson(f, a+((j-1)*dx), a+(j*dx), 4)

      j = j + 1

    return antiderivative[:-1], x_values

def f(x):
    # Replace zero values in x with a small positive value to avoid division by zero
    x_safe = np.where(x == 0, np.finfo(float).eps, x)

    return np.exp(-1 / x_safe)

def g(x):
    # Replace zero values in x with a small positive value to avoid division by zero
    x_safe = np.where(x == 0, np.finfo(float).eps, x)

    return np.cos(1 / x_safe)

def h(x):
  return (x*x*x)+(1/2)

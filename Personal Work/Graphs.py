import matplotlib.pyplot as plt
import numpy as np


def quadratic_function(x):
    a = 1
    b = 2
    c = 1
    y = a * x ** 2 + b * x + c
    return y


x = np.linspace(-5, 5, 100)
y = quadratic_function(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Function')
plt.show()

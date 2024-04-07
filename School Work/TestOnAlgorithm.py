import numpy as np
import matplotlib.pyplot as plt

you_are_done = False
closes_value = 0
def finite_difference_derivative(f, x, h=0.0001):
    return (f(x + h) - f(x - h)) / (2 * h)

def find_stationary_points(f, start, end, step_size=0.01, tol=0.006):
    global closes_value, you_are_done
    stationary_points = []
    x = start
    while x < end:
        derivative = finite_difference_derivative(f, x)
        if abs(derivative) < tol:
            stationary_points.append(x)
            closes_value = f(x)
        if f(x) == 0:
            you_are_done = True
        x += step_size

    return stationary_points

def plot_function_and_points(f, stationary_points, x_range=(-1, 4)):
    x = np.linspace(*x_range, 1000)  # Increase resolution for smooth plot
    y = f(x)

    plt.plot(x, y, label='Function')
    plt.scatter(stationary_points, [f(point) for point in stationary_points], marker='o', c='red', label='Stationary Points')
    print(stationary_points)
    plt.legend()
    plt.show()

# Example usage:
def f(x):
    return x**3-9*x**2+14*x+32 - (16+14.9*x-4.9*x**2)
# Replace with your desired function

start = 0
end = 10


stationary_points = find_stationary_points(f, start, end, step_size=0.001)
print(you_are_done,closes_value)

plot_function_and_points(f, stationary_points, x_range=(start, end))


import matplotlib.animation as ani
import matplotlib.collections as cl
import matplotlib.pyplot as plt

carMatrix = [[0, 0], [0, 1], [1, 1], [1, 0]]

carX = 0.5
carY = 0.5
carAngle = 0

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)


def matrix_to_line(matrix):
    matrix.append(matrix[0])
    lines = []
    for i in range(len(matrix) - 1):
        lines.append([matrix[i], matrix[i + 1]])
    return lines


def detect_move():
    global carMatrix
    up = [[1, 0] for i in range(4)]
    carMatrix += up
    yield carMatrix


def plot_car(data):
    lineCollection = cl.LineCollection(matrix_to_line(carMatrix), linewidths=2)
    ax.add_collection(lineCollection)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.margins(0.1)
    return ax


if __name__ == '__main__':
    while True:
        updateAnimation = ani.FuncAnimation(fig, plot_car, detect_move, interval=100)
        plt.show()

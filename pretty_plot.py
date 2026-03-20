#necessary import statements
import numpy as np
import matplotlib.pyplot as plt

#calculate the needed points
def generate_points(matrix, initial_point):
    points = [initial_point]

    for i in range(250):
        new_point = matrix @ points[-1]
        points.append(new_point)

    return np.array(points)

#plot the points in the figure
def plot_points(points):
    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], linestyle='dashed')
    #title and label each axis
    plt.title("Spiral in a shape resembling a Fibonacci Sequence")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()

#set the initial point and matrix values
matrix = np.array([[1.02, 0.095], [-0.095, 1.02]])
initial_point = np.array([0, 1])

#show output
pointsToShow = generate_points(matrix, initial_point)
plot_points(pointsToShow)

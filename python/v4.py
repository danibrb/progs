import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from PIL import Image


def generate_point_cloud(image, d):
    image_array = np.array(image.convert('L'))  # Convert image to grayscale numpy array

    points = []

    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            shade = image_array[i][j]

            if not any(np.linalg.norm(np.array([i, j]) - np.array(p)) < d for p in points):
                points.append([i, j])

    return np.array(points)


def find_path(point_cloud):
    start_point = point_cloud[np.argmin(point_cloud[:, 1])]
    end_point = point_cloud[np.argmax(point_cloud[:, 1])]

    path = [start_point]

    while not np.array_equal(path[-1], end_point):
        p1 = path[-1]
        found_neighbor = False

        for n in point_cloud:
            if np.array_equal(n, path[-1]):
                continue

            if n.tolist() not in path and not does_cross_existing_edge(path[-1], n, path):
                path.append(n)
                found_neighbor = True
                break

        if not found_neighbor:
            break

    return np.array(path)


def does_cross_existing_edge(p1, p2, path):
    for i in range(len(path) - 1):
        if intersect(p1, p2, path[i], path[i + 1]):
            return True
    return False


def intersect(p1, p2, q1, q2):
    d1 = np.cross(p2 - p1, q1 - p1)
    d2 = np.cross(p2 - p1, q2 - p1)
    d3 = np.cross(q2 - q1, p1 - q1)
    d4 = np.cross(q2 - q1, p2 - q1)

    if np.sign(d1) != np.sign(d2) and np.sign(d3) != np.sign(d4):
        return True
    elif d1 == 0 and on_segment(p1, p2, q1):
        return True
    elif d2 == 0 and on_segment(p1, p2, q2):
        return True
    elif d3 == 0 and on_segment(q1, q2, p1):
        return True
    elif d4 == 0 and on_segment(q1, q2, p2):
        return True

    return False


def on_segment(p, q, r):
    return min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and min(p[1], q[1]) <= r[1] <= max(p[1], q[1])


def smooth_path(path):
    t = np.linspace(0, len(path) - 1, 100)
    spline = make_interp_spline(np.arange(len(path)), path.T, k=3)
    smooth_path = spline(t)
    return smooth_path


# Example usage
image_path = 'images.jpg'  # Replace with the path to your image file
d = 20  # Distance parameter

# Open image file
image = Image.open(image_path)

# Generate point cloud from the image
point_cloud = generate_point_cloud(image, d)

# Find Hamiltonian-like path
path = find_path(point_cloud)

# Smooth the path
smoothed_path = smooth_path(path)

# Plot the point cloud and path
plt.scatter(point_cloud[:, 0], point_cloud[:, 1], color='red', label='Points')
plt.plot(smoothed_path[:, 0], smoothed_path[:, 1], color='blue', label='Path')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Hamiltonian-like Path')
plt.show()
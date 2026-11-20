from matplotlib import pyplot as plt
import numpy as np
from calculate_position import *

def visualize_movement():
    """
    plot yo shit twin
    """
    x_coords = []
    y_coords = []

    current_lengths = (1035.0, 995.0)
    points = [(914.0, -400.0, 0), (914.0, -600.0, 1), (445.0, -488.0, 1), (1340.0, -643.0, 1)]

    for point in points:
        point = point[:-1]
        current_pos, _ = calculate_position_from_lengths(*current_lengths)
        subpoints = space_points_linearly(current_pos, point)

        for subpoint in subpoints:
            current_pos, phi = calculate_position_from_lengths(*current_lengths)
            x_coords.append(current_pos[0])
            y_coords.append(current_pos[1])
            next_lengths = calculate_next_position(*subpoint, phi)
            # diff_lengths = calculate_position_difference(current_lengths, next_lengths)
            # MOVE BY LENGTH DIFFERENCE
            current_lengths = next_lengths
    
    plt.figure()
    plt.plot(x_coords, y_coords, 'r.')
    plt.plot([pt[0] for pt in points], [pt[1] for pt in points], 'b.')
    plt.xlim(0, 1829)
    plt.ylim(-1500, 0)
    plt.show()


def simulate_sensors(pos):
    """
    estimate sensor readings at a given position
    """


if __name__ == "__main__":
    #visualize_movement()
    visualize_movement()
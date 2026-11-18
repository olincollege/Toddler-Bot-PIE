from matplotlib import pyplot as plt
import numpy as np
from calculate_position import *

def visualize_movement():
    """
    plot yo shit twin
    """
    initial = (910, 640)
    points = [(914.0, -400.0, 0), (914.0, -600.0, 1), (445.0, -488.0, 1), (1340.0, -643.0, 1)]

    for point in points:
        current_pos = initial
        subpoints = space_points_linearly(current_pos, point)
        phi_initial = 0

        for subpoint in subpoints:
            theta_l = 0 #left encoder reading
            theta_r = 0 #right encoder reading
            phi = 0 #IMU reading
            current_pos, current_lengths = calculate_current_position(theta_l, theta_r, phi)
            next_lengths = calculate_next_position(*subpoint, phi)
            diff_lengths = calculate_position_difference(current_lengths, next_lengths)
            # MOVE BY LENGTH DIFFERENCE
    
        initial = point


def simulate_sensors(pos):
    """
    estimate sensor readings at a given position
    """
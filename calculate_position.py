"""
Contains functions to calculate current and next positions of Toddler Bot,
and how to get from one position to the next.
"""

from math import pow, sqrt, sin, cos
from numpy import arctan2, array
from numpy.linalg import lstsq

def calculate_current_lengths(theta_l, theta_r, phi):
    """
    Uses string angles and tilt to calculate the string lengths at the bot's current position.

    Args:
        theta_l (double): Acute angle of left string, in radians.

        theta_r (double): Acute angle of right string, in radians.

        phi (double): Tilt angle, in radians. Positive represents a clockwise tilt.
    
    Returns:
        (numpy.ndarray): String lengths, in mm, in a 2x1 array. Left then right.

    """
    # define constants
    w = 157.48  # mm
    h = 40.64  # mm
    x_end = 2000  # mm
    winch_to_marker_dist = sqrt(pow(h,2) + pow(w,2)/4)  # mm
    winch_to_marker_angle = arctan2(h, w/2)  # rads

    # calculate string lengths
    A = array([[-sin(theta_l), sin(theta_r)],
               [cos(theta_l), cos(theta_r)]])
    b = array([[w*sin(phi)],
              [x_end - w*cos(phi)]])
    return lstsq(A, b)[0]

def calculate_next_position(x, y):
    """
    Uses marker x and y coordinates to calculate string lengths at a future position.

    Args:
        x (double): Final x position of marker.

        y (double): Final y position of marker.

    Returns:
        (numpy.ndarray): Final string lengths, in mm, in a 2x1 array. Left then right.
    """
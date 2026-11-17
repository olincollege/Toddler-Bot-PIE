"""
Contains functions to calculate current and next positions of Toddler Bot,
and how to get from one position to the next.
"""

from math import sqrt, sin, cos
from numpy import arctan2, array
from numpy.linalg import lstsq, norm
from scipy.constants import g as g_m
from sympy import Symbol, diff, nsolve, sin as symsin, cos as symcos


def calculate_current_position(theta_l, theta_r, phi):
    """
    Uses string angles and tilt to calculate the string lengths at the bot's current position.

    Args:
        theta_l (double): Acute angle of left string, in radians.

        theta_r (double): Acute angle of right string, in radians.

        phi (double): Tilt angle, in radians. Positive represents a clockwise tilt.
    
    Returns:
        (tuple): Tuple of tuples. One has string lengths in mm, the other has the marker coordinates.

    """
    # define constants
    w = 157.48  # mm
    h = 40.64  # mm
    x_end = 2000  # mm
    winch_to_marker_dist = sqrt(h^2 + w^2/4)
    winch_to_marker_angle = arctan2(h, w/2)

    # calculate string lengths
    A = array([[-sin(theta_l), sin(theta_r)],
               [cos(theta_l), cos(theta_r)]])
    b = array([[w*sin(phi)],
              [x_end - w*cos(phi)]])
    s = lstsq(A, b)[0]

    # calculate left winch position
    x_l = s[0][0]*cos(theta_l)
    y_l = -s[0][0]*sin(theta_l)

    # calculate marker position
    x = x_l + cos(phi + winch_to_marker_angle)*winch_to_marker_dist
    y = y_l - sin(phi + winch_to_marker_angle)*winch_to_marker_dist

    return tuple(s.transpose().tolist()[0]), (x_l, y_l)


def calculate_next_position(x, y):
    """
    Uses marker x and y coordinates to calculate string lengths at a future position.

    Args:
        x (double): Final x position of marker.

        y (double): Final y position of marker.

    Returns:
        (tuple): Final string lengths, in mm, in a 2-element tuple. Left then right.
    """
    # define constants
    g = g_m * 10**3  # mm/s^2
    k = 100  # N/mm
    m = 1  # kg
    w = 157.48  # mm
    h = 40.64  # mm
    x_end = 2000  # mm
    y_end = 2000  # mm
    winch_to_marker_dist = sqrt(h**2 + w**2/4)  # mm
    winch_to_marker_angle = arctan2(h, w/2)  # rads

    # define symbolic position expressions
    phi = Symbol('phi', real=True)
    x_l = x - symcos(phi + winch_to_marker_angle)*winch_to_marker_dist
    y_l = y + symsin(phi + winch_to_marker_angle)*winch_to_marker_dist
    x_r = x_l + w*symcos(phi)
    y_r = y_l - w*symsin(phi)

    # define symbolic potential energy expressions
    PE_x = k*0.5*(x_l**2 + (x_end - x_r)**2)
    PE_y = k*0.5*((y_l + y_end)**2 + (y_r + y_end)**2) - m*g*(y_l + y_r + 2*y_end)
    PE_sum = PE_x + PE_y

    # define and find root of derivative of potential energy with respect to phi
    dPE = diff(PE_sum, phi)
    tilt = nsolve(dPE, phi, 0)

    # substitute tilt into other position expressions
    x_l_real = x_l.subs(phi, tilt)
    x_r_real = x_r.subs(phi, tilt)
    y_l_real = y_l.subs(phi, tilt)
    y_r_real = y_r.subs(phi, tilt)

    # calculate and return string lengths
    s_l = sqrt(x_l_real**2 + y_l_real**2)
    s_r = sqrt((x_end - x_r_real)**2 + y_r_real**2)
    return s_l, s_r


def calculate_position_difference(s_initial, s_final):
    """
    Calculates the difference in string lengths between two points

    Args:
        s_initial (tuple): String lengths at initial position, in mm, in a 2-element tuple.

        s_final (tuple): String lengths at final position, in mm, in a 2-element tuple.

    Returns:
        (tuple): Differences in string lengths between final and initial positions.
    """
    x_diff = s_final[0] - s_initial[0]
    y_diff = s_final[1] - s_initial[1]
    return x_diff, y_diff


def split_points_list(dist, length=5.0):
    """
    returns list of points with much smaller distances
    """
    abs_dist = (abs(dist[0]), abs(dist[1]))
    steps = max(abs_dist)//length
    diffs = []
    sums = [0.0, 0.0]
    dx = max(abs(abs_dist[0]/steps), 0.5)
    dy = max(abs(abs_dist[1]/steps), 0.5)

    for _ in range(int(steps)):
        if sums[0]+dx >= abs_dist[0] and sums[1]+dy >= abs_dist[1]:
            diffs.append((abs_dist[0]-sums[0], abs_dist[1]-sums[1]))
            break
        elif sums[0]+dx >= abs_dist[0]:
            diffs.append((abs_dist[0]-sums[0], dy))
            while sums[1]+dy < abs_dist[1]:
                diffs.append((0, dy))
                sums[1] += dy
            diffs.append((0, abs_dist[1]-sums[1]))
            break
        elif sums[1]+dy >= abs_dist[1]:
            diffs.append((dx, abs_dist[1]-sums[1]))
            while sums[0]+dx < abs_dist[0]:
                diffs.append((dx, 0))
                sums[0] += dx
            diffs.append((abs_dist[0]-sums[0], 0))
            break

        diffs.append((dx, dy))
        sums[0] += dx
        sums[1] += dy

    if dist[0] < 0 and dist[1] < 0:
        return [(-diff[0], -diff[1]) for diff in diffs]
    if dist[0] < 0:
        return [(-diff[0], diff[1]) for diff in diffs]
    if dist[1] < 0:
        return [(diff[0], -diff[1]) for diff in diffs]
    return diffs

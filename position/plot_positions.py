from matplotlib import pyplot as plt
import numpy as np
from calculate_position import *

def visualize_movement():
    """
    plot yo shit twin
    """
    

    initial = (910, 640)
    points = [(914.0, -400.0, 0), (914.0, -600.0, 1), (445.0, -488.0, 1), (1340.0, -643.0, 1)]
    points.insert(0, initial)
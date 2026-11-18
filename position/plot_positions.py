from matplotlib import pyplot as plt
import numpy as np
from calculate_position import *

def plot_y_error():
    """
    plot error on y axis
    """
    x_range = np.arange(100, 1700, 100)
    y_error = np.zeros(x_range.shape)
    for i in range(x_range.size):
        sum = 0
        for y in range(-2000, -500, 100):
            lengths = calculate_next_position(x_range[i], y)
            pos = calculate_position_from_lengths(*lengths)
            sum += pos[1] - y
        y_error[i] = sum/15

    # fit to polynomial
    params = np.polyfit(x_range, y_error, 3)
    fit = lambda x: np.array([params[len(params)-1-i]*(x**i) for i in range(len(params))]).sum()
    y_error_predicted = [fit(x) for x in x_range]
    print(params)

    plt.figure()
    plt.plot(x_range, y_error, 'r.-')
    plt.plot(x_range, y_error_predicted, 'b.-')
    plt.show()


def plot_points():
    """
    plot actual points and where estimations end up
    """
    actual = [(x, -y) for y in range(500, 2000, 100) for x in range(100, 1700, 100)]
    plt.figure()
    for a in actual:
        lengths = calculate_next_position(*a) #(1035.0, 995.0)
        pos = calculate_position_from_lengths(*lengths)
        plt.plot([a[0], pos[0]], [a[1], pos[1]], 'b-')
        plt.plot(*a, 'r.')
        plt.plot(*pos, 'b.')
        #print(f"{a} -> {pos}")

    plt.xlim((0, 1829))
    plt.ylim((-2000, 0))
    plt.show()


def plot_surf():
    """
    plot surface of error
    """
    l = np.arange(900, 1700, 100)
    r = np.arange(900, 1700, 100) # DON'T GO ABOVE -500
    lgrid, rgrid = np.meshgrid(l, r)
    ugrid = np.zeros(lgrid.shape)
    ugrid_corr = np.zeros(lgrid.shape)
    vgrid = np.zeros(lgrid.shape)
    vgrid_corr = np.zeros(lgrid.shape)
    for i in range(lgrid.shape[0]):
        for j in range(lgrid.shape[1]):
            dist = sqrt((0.5*lgrid[i,j])**2 + (0.8*rgrid[i,j])**2)
            pos = calculate_position_from_lengths(lgrid[i,j], rgrid[i,j])
            pred = calculate_next_position(*pos)
            ugrid[i,j] = pred[0] - lgrid[i,j]
            vgrid[i,j] = pred[1] - rgrid[i,j]
            ugrid_corr[i,j] = -0.8*dist + 1200
            #vgrid_corr[i,j] = 2.3*dist

    #ugrid_corr -= (ugrid + ugrid_corr).mean()
    #vgrid_corr -= (vgrid + vgrid_corr).mean()
    #print((ugrid + ugrid_corr).mean())
    #print((vgrid + vgrid_corr).mean())

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(lgrid, rgrid, ugrid, label="l")
    #ax.plot_surface(lgrid, rgrid, vgrid, label="r")
    ax.plot_surface(lgrid, rgrid, ugrid + ugrid_corr, label="x_corrected")
    #ax.plot_surface(xgrid, ygrid, vgrid + vgrid_corr, label="y_corrected")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('error')
    plt.legend()
    plt.show()


#plot_y_error()
plot_points()
# import of the package
# for the mathematical computation
import numpy as np
# import for the plot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
# importing the odeint package to resolv our equation
from scipy.integrate import odeint
from functions import *


    
    # the main function to run, 
def main():
# defining our rate and constant
# alpha(fish groth rate), beta(algae rate groth), omax (max amount of o2)
    args = [1.1, 1.6, 0.5, 0.5, 0.004, 300, 1000, 100, 2000]
    # definding our initial value
    y0 = [500, 25, 300]
    # definding our time vector, basicly its the time axys values
    t = np.linspace(0,100,1001)
    draw_phase_space (y0, args)


if __name__ == '__main__':
    main()
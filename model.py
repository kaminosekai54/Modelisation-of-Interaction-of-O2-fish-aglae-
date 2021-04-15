# import of the package
# for the mathematical computation
import numpy as np
# import for the plot
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
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
    t = np.linspace(3000, 3001)                   #set the timespan for the simulation#
    #  We call the odeint methode to solve the differential equation
    model = odeint(compute_derivative, y0, t, args = (args,))  

# plotting the result.
    plt.plot(t, model[:,0], 'r', label='Disolve O2')
    plt.plot(t, model[:,1], 'b', label='Fish amount')
    plt.plot(t, model[:,2], 'g', label='Alga amount')
    plt.xlabel('time')
    plt.ylabel('Amount')
    plt.title('evolution of O2, Fish and Alga')
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
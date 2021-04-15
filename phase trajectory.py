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
    t = np.linspace(0,100,1001)                   #set the timespan for the simulation#
    #  We call the odeint methode to solve the differential equation
    model = odeint(compute_derivative, y0, t, args = (args,))  

# plotting the result.

    fig = plt.figure() 
    ax = fig.add_subplot(projection='3d')
    ax.plot(model[:,0], model[:,1], model[:,2])
    ax.set_xlabel('O2')
    ax.set_ylabel('Fish')
    ax.set_zlabel('Algae')
    plt.show()

if __name__ == '__main__':
    main()
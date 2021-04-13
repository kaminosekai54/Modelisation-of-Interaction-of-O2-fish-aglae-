# import of the package
# for the mathematical computation
import numpy as np
# import for the plot
import matplotlib.pyplot as plt
# importing the odeint package to resolv our equation
from scipy.integrate import odeint



#  function compute_derivative
# This function compute the derivative wanted to study the model 
# @param
# @y, a list containing the initial concentration values for our reactances and product
# @t, a list of time range, mostly useful for the odeint function
# @args, a list containing all the different constant we need
def compute_derivative(y0, t, args):
	# initialising our value
    # storing the different value of args into variables
    # the variable are named according to their name in the equation 
    #they represent the different rates and constant
    alpha, beta, c, P, g, pmax, amax, omin  = args
    # storing the different value of y into variables
    # they are named according to their name into the equation 
    # they represent the different initial value for the model
    o, p, a = y0

	# writing our derivative
    dodt = P * a - c*p
    dpdt = (alpha* p)  * (1- (p/pmax))
    dadt = (beta * a) * (1- (a/amax))

    #  return of the computed derivative in a list
    return [dodt, dpdt, dadt]
	
	# the main function to run, 
def main():
# defining our rate and constant
# alpha(fish groth rate), beta(algae rate groth), c(o2 consumation by fish), P(production rate of O2), g(amount of eaten algae by a fish)), pmax(max amount of fish), amax(max amount of algae), omin(minimum required for fish to leave)  
	args = [1.02, 1.004, 0.1, 0.2, 2, 500, 2000, 100]
	# definding our initial value
	y0 = [1000, 50, 1000]
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
	plt.show()                            #we plot the graph presenting the concentrations depending on time 

if __name__ == '__main__':
	main()


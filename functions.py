# This file is composed of the usefull function
################################################

# import of the package
# for the mathematical computation
import numpy as np
# import for the plot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
# importing the odeint package to resolv our equation
from scipy.integrate import odeint

#  function compute_derivative
# This function compute the derivative wanted to study the model 
# @param
# @y0, a list containing the initial value for the variable of the model
# @t, a time , mostly useful for the odeint function
# @args, a list containing all the different the parameter of the model (rate, constant, etc, etc)
def compute_derivative(y0, t, args):
    # initialising our value 
    # storing the different value of args into variables
    # the variable are named according to their name in the equation 
    #they represent the different rates and constant
    # defining our rate and constant
# alpha(fish groth rate), beta(algae rate groth), omax (max amount of o2)
    alpha, beta, c, P, g, pmax, amax, omin, omax  = args
    # storing the different value of y into variables
    # they are named according to their name into the equation 
    # they represent the different initial value for the model
    # o (initial value of O2, p initial value of fish, a initial value of algae)
    o, p, a = y0

    # writing our derivative
    dodt = (0.0001*o*(P * a - c*p))*(1-(o/omax))
    # fo is a function of o and p we defined it to be 0 if the computation give us a result is >= 0 to make o2 have a negative influence only when its under a certain value
    fo = ((o - p*c) - omin) / c
    if fo >= 0 :
        fo = 0
    dpdt = (0.01*p*((alpha* p)  * (1- (p/pmax))  + fo))
    dadt = (beta * a) * (1- (a/amax)) - p*g*a

    #  return of the computed derivative in a list
    return [dodt, dpdt, dadt]



# function draw_phase_space ,
# This function will draw a vector field representing our model
#@param,
#@y0, the list of initial value for the model (Usefull for the computations)
#@args, a list of parameter for the model (Usefull for the computation)
def draw_phase_space (y0, args):
    # creating different vectors, representing our variables

    t = np.linspace(1,200,10)
    o_vector = np.linspace(1,200,10)
    p_vector = np.linspace(1,200,10)
    a_vector = np.linspace(1,200,10)
    o_n,p_n,a_n = np.meshgrid(o_vector, p_vector, a_vector)
    aux1 = np.zeros(o_n.shape)
    aux2 = np.zeros(p_n.shape)
    aux3 = np.zeros(a_n.shape)

# looping and computing our values for T = 0
    for i in range (0,len(o_vector)):
        for j in range (0,len(p_vector)):
            for k in range (0,len(a_vector)):
                dodt, dpdt, dadt = compute_derivative((o_vector[i], p_vector[j],a_vector[k]),0,args)
                aux1[i,j,k] = dodt
                aux2[i,j,k] = dpdt
                aux3[i,j,k] = dadt

                # creating the figure
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.invert_xaxis()
    ax.quiver(o_n, p_n, a_n, aux1, aux2, aux3)
    ax.set_xlabel("O2") # x label 
    ax.set_ylabel("Fish population") # y label
    ax.set_zlabel("Algae population")

    # solving our ODE using odeint
    model = odeint(compute_derivative, y0, t, args = (args,)) 
    ax.plot(model[:,0], model[:,1], model[:,2], 'r')
    ax.set_xlabel("O2") # x label 
    ax.set_ylabel("Fish") # y label
    ax.set_zlabel("Algae")
    # showing the result
    plt.show()
    return "We liked this project"
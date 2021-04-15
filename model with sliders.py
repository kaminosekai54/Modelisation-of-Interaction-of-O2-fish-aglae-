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
# alpha(fish groth rate), beta(algae rate groth), c(o2 consumation by fish), P(production rate of O2), g(amount of eaten algae by a fish)), pmax(max amount of fish), amax(max amount of algae), omin(minimum required for fish to leave), omax (the maximal quantity of O2) 
    args = [1.1, 1.6, 0.5, 0.5, 0.004, 300, 1000, 100, 2000]
    # definding our initial value
    y0 = [500, 25, 300]
    # definding our time vector, basicly its the time axys values
    t = np.linspace(0,100,1001)                   #set the timespan for the simulation#
    #  We call the odeint methode to solve the differential equation
    model = odeint(compute_derivative, y0, t, args = (args,))  

# plotting the result.
    fig,g=plt.subplots()
    plt.subplots_adjust(bottom=0.60)
    axis_color = 'lightgoldenrodyellow'
                           #we plot the graph presenting the concentrations depending on time


        # Define an axes area and draw a slider in it
    o2_slider_ax  = fig.add_axes([0.25, 0.05, 0.65, 0.02], facecolor=axis_color)
    o2_slider = Slider(o2_slider_ax, 'O2', 0, 50000, valinit=y0[0])

    p_slider_ax  = fig.add_axes([0.25, 0.10, 0.65, 0.02], facecolor=axis_color)
    p_slider = Slider(p_slider_ax, 'Fish', 0, 50000, valinit=y0[1])
    a_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.02], facecolor=axis_color)
    a_slider = Slider(a_slider_ax, 'Algae', 0, 50000, valinit=y0[2])

    t_slider_ax  = fig.add_axes([0.25, 0.20, 0.65, 0.02], facecolor=axis_color)
    t_slider = Slider(t_slider_ax, 't', 0, 10, valinit=1)

    c_slider_ax = fig.add_axes([0.25, 0.25, 0.65, 0.02], facecolor=axis_color)
    c_slider = Slider(c_slider_ax, 'Fish O2 consumation', 0.00, 2.5, valinit=args[2])

    P_slider_ax = fig.add_axes([0.25, 0.30, 0.65, 0.02], facecolor=axis_color)
    P_slider = Slider(P_slider_ax, 'Algae O2 production', 0.5, 2.5, valinit= args[3])

    g_slider_ax = fig.add_axes([0.25, 0.35, 0.65, 0.02], facecolor=axis_color)
    g_slider = Slider(g_slider_ax, 'Fish algae consumation', 0.5, 100, valinit=args[4])

    pmax_slider_ax = fig.add_axes([0.25, 0.40, 0.65, 0.02], facecolor=axis_color)
    pmax_slider = Slider(pmax_slider_ax, 'Max fish', 2, 5000, valinit=args[5])


    amax_slider_ax = fig.add_axes([0.25, 0.45, 0.65, 0.02], facecolor=axis_color)
    amax_slider = Slider(amax_slider_ax, 'Max Algae', 2, 5000, valinit=args[6])

    omin_slider_ax = fig.add_axes([0.25, 0.50, 0.65, 0.02], facecolor=axis_color)
    omin_slider = Slider(omin_slider_ax, 'minimum O2 required', 2, 2000, valinit=args[7])

    curv1, = g.plot(t, model[:,0], 'r', label='Disolved O2')
    curv2, = g.plot(t, model[:,1], 'b', label='Fish amount')
    curv3, = g.plot(t, model[:,2], 'g', label='Alga amount')

    def sliders_on_changed(val):
        y0[0] = o2_slider.val
        y0[1] = p_slider.val
        y0[2] = a_slider.val
        args[2] = c_slider.val
        args[3] = P_slider.val
        args[4] = g_slider.val
        args[5] = pmax_slider.val
        args[6] = amax_slider.val
        args[7] = omin_slider.val
        args[7] = omin_slider.val
        t = np.linspace(0,int(t_slider.val),int(t_slider.val)+1)
        g.set_xlim(0,int(t_slider.val)+0.25)
        model = odeint(compute_derivative, y0, t, args = (args,)) # solve the differential equation 
        curv1.set_xdata(t) 
        curv2.set_xdata(t)
        curv3.set_xdata(t)
        curv1.set_ydata(model[:,0])
        curv2.set_ydata(model[:,1])
        curv3.set_ydata(model[:,2])

    t_slider.on_changed(sliders_on_changed)
    o2_slider.on_changed(sliders_on_changed)
    p_slider.on_changed(sliders_on_changed)
    a_slider.on_changed(sliders_on_changed)
    c_slider.on_changed(sliders_on_changed)
    P_slider.on_changed(sliders_on_changed)
    g_slider.on_changed(sliders_on_changed)
    pmax_slider.on_changed(sliders_on_changed)
    amax_slider.on_changed(sliders_on_changed)
    omin_slider.on_changed(sliders_on_changed)

    reset_button_ax = fig.add_axes([0.05, 0.2, 0.1, 0.04])
    reset_button = Button(reset_button_ax, 'Reset', color=axis_color, hovercolor='0.975')
    def reset_button_on_clicked(mouse_event):
        c_slider.reset()
        P_slider.reset()
        g_slider.reset()
        pmax_slider.reset()
        amax_slider.reset()
        omin_slider.reset()
        o2_slider.reset()
        p_slider.reset()
        a_slider.reset()
        t_slider.reset()
    reset_button.on_clicked(reset_button_on_clicked)        
    g.set_xlabel('Time')
    g.set_ylabel('Amount')
    g.set_title('evolution of O2, Fish and Alga')
    plt.show()

if __name__ == '__main__':
    main()
import brian2 as b2
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1234)

def g(x):
    """ Implementation of the gain fucntion. """
    if x <= 0:
        y = 0
    elif x > 0 and x < 1:
        y = x
    else:
        y = 1
    return y

def behaviour_model(
    time,
    dt = 0.01,
    b1 = 0.8, b2 = 0.8,
    w_ee = 3.0,
    alpha = 1., sigma = .5
    ):
    """ Implementation of the behaviour model.

    Parameters
    ----------
    time : np.array
        Duration that the simulation will run
    b1 : float
        Stimuli intensity to the population 1.
    b2 : float
        Stimuli intensity to the population 2.
    w_ee : float
        Selft-excitation parameter.
    alpha : float
        Inhibition parameter.
    sigma : float
        Noise level. 
    """    
    #: duration
    duration = int(time/dt)
    #: matrix containing the population dynamics
    h = np.zeros((2, duration))

    for t in range(duration - 1):
        #: h1 
        h[0][t+1] =  h[0][t] + dt * (-h[0][t] + b1 + (w_ee - alpha)*g(h[0][t]) - alpha*g(h[1][t])) + \
        np.sqrt(dt)*sigma*np.random.normal()
        #: h2 
        h[1][t+1] =  h[1][t] + dt * (-h[1][t] + b2 + (w_ee - alpha)*g(h[1][t]) - alpha*g(h[0][t])) + \
        np.sqrt(dt)*sigma*np.random.normal()
    return h

def plot_results(h, time, ax = None):
    """ Plot the population dynamics. 
    
    Parameters
    ----------
    h : np.array (2, Length)
        Matrix containing the population dynamics.
    time: np.array
        Time 
    """
    if ax is None:
        ax = plt.gca()

    ax.plot(time, h[0][:], label='first population')
    ax.plot(time, h[1][:], label='second population')
    ax.set_title('Time evolution of parameters')
    plt.legend()

def main():
    """Main."""
    duration = 10
    dt = 0.01
    h = behaviour_model(duration)
    fig, ax = plt.subplots(figsize = (10,6))
    plot_results(h, np.arange(0, duration, dt), ax=ax)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Membrane potential (mV)')
    plt.show()



if __name__ == '__main__':
    main()
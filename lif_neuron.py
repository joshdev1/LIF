import numpy as np
import matplotlib.pyplot as plt


def lif_neuron(I, dt, T, tau):
    E = -0.065
    R = 10e6
    v_0 = -0.07
    v_thresh = -0.05
    v_reset = -0.067
    time = np.arange(0, T+dt, dt)
    spikes = np.zeros(len(time))
    v = np.zeros(len(time))

    v[0] = v_0
    for i in range(len(time)-1):
        dv = dt * (E - v[i] + R * I)/tau
        v[i+1] = v[i] + dv
        if v[i+1] > v_thresh:
            spikes[i] = 1
            v[i+1] = v_reset
    rate = sum(spikes) / 1.5
    return spikes, rate, v, time


def graph_output(time, membrane_voltage):
    plt.figure(figsize=(15, 7))
    plt.plot(time, membrane_voltage, color=u'#FFBB6C', label='Voltage')
    plt.legend(loc=1)
    plt.grid()
    plt.title('Leaky Integrate-and-Fire Neuron')
    plt.ylabel('Membrane Potential (Vm)')
    plt.xlabel('Time (msec)')
    plt.show()


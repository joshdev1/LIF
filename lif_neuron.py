import numpy as np


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
    return spikes, rate

import numpy as np
import matplotlib.pyplot as plt


class LIFNeuron:
    def __init__(self, I, dt, T, tau):
        self.I = I
        self.dt = dt
        self.T = T
        self.tau = tau
        self.E = -0.065
        self.R = 10e6
        self.v_0 = -0.07
        self.v_thresh = -0.05
        self.v_reset = -0.067
        self.time = np.arange(0, T+dt, dt)
        self.spikes = np.zeros(len(self.time))
        self.v = np.zeros(len(self.time))

    def run_neuron(self):
        self._set_initial_membrane_voltage()
        for i in range(len(self.time)-1):
            self._get_membrane_voltage(i)
            self._check_spike_threshold(i)

    def get_rate(self):
        return sum(self.spikes) / 1.5

    def _set_initial_membrane_voltage(self):
        self.v[0] = self.v_0

    def _get_membrane_voltage(self, i):
        dv = self.dt * (self.E - self.v[i] + self.R * self.I) / self.tau
        self.v[i + 1] = self.v[i] + dv

    def _check_spike_threshold(self, i):
        if self.v[i + 1] > self.v_thresh:
            self.spikes[i] = 1
            self.v[i + 1] = self.v_reset

    def graph_output(self):
        plt.figure(figsize=(15, 7))
        plt.plot(self.time, self.v, color=u'#FFBB6C', label='Voltage')
        plt.legend(loc=1)
        plt.grid()
        plt.title('Leaky Integrate-and-Fire Neuron')
        plt.ylabel('Membrane Potential (Vm)')
        plt.xlabel('Time (msec)')
        plt.show()

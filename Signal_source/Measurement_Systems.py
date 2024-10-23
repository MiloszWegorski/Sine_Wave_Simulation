import numpy as np
from Signal_source.Measurement_schemes import Uniform_Measurement
from Signal_source.Model_signals import Sine_wave
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt

class Measurement_device(ABC):

    def Measure(self):

        return np.array(self._Measure())
    
    @abstractmethod
    def _Measure(self):
        pass
        
    def get_name(self):
        return self._get_name(self)
    
    @abstractmethod
    def _get_name(self):
        pass


class Measure_Normal_Sine(Measurement_device):

    def __init__(self, scheme:Uniform_Measurement, signal:Sine_wave):
        self.scheme = scheme
        self.signal = signal

    
    def _Measure(self):
        times = self.scheme.get_points()
        
        return [np.array(times), np.array(self.signal.get_amplitudes(times))]
    
    def _get_name(self):
        return f'I measure a normal sine wave'
import numpy as np
from abc import ABC, abstractmethod

class Model_signal(ABC):

    def get_amplitudes(self, times):
        return np.array(self._get_amplitudes(times))
    
    @abstractmethod
    def _get_amplitudes(self, times):
        pass
    
    def get_name(self):
        return self._get_name()
    
    @abstractmethod
    def _get_name(self):
        pass


class Sine_wave(Model_signal):
    
    def __init__(self, freq, amp, phase ,offset):

        self.frequency = freq
        self.amplitude = amp
        self.phase = phase
        self.offset = offset

        self.name = f"Returns a perfect sinousidal wave"

    def _get_amplitudes(self, times):

        return self.amplitude * np.sin(2 * times * np.pi * self.frequency + 
                                       self.phase) + self.offset
    
    def _get_name(self):
        return self.name
import numpy as np
from abc import ABC, abstractmethod

class noise(ABC):

    def noisify(self, amplitudes):
        return np.array(self._noisify(amplitudes))
    
    @abstractmethod
    def _noisify(self, amplitudes):
        pass

    def get_name(self):
        return self.name
    

class Gaussian_noise(noise):

    def __init__(self, noise_level : float) -> None:
        
        self.noise_level = noise_level

        self.name = f""

    def _noisify(self, amplitudes : np.array):
        
        noise = np.random.normal(-self.noise_level, self.noise_level, 
                                 len(amplitudes))
        
        noisy_amps = np.empty_like(amplitudes)
        
        for i, j in zip(noise, range(len(amplitudes))):
            noisy_amps[j] = i + amplitudes[j]

        return noisy_amps

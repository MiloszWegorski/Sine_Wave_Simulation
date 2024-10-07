import numpy as np

def sin_func( time:list[float], amp: float, freq: float, phase: float, offset: float):
    return amp* np.sin(time * +2 * np.pi * freq + phase) + offset

class Signal:
    """
    Object which generates Signal measurement points according to the 
    signal and measurement scheme with applied noise from the noisifier
    objects to change these call their respective setters
    """
    def __init__(self):
        """
        Args:
            freq (float): Frequency
            phase (float): Phase
            amp (float): amplitude
            offset (float): amplitude offset
            time (float): time for which the wave propagates
        """
        self.frequency = 5
        self.phase = 0
        self.amplitude = 1
        self.offset = 0

    def get_measurements(self):

        measure_scheme = Measurement_scheme.get_scheme()

        signal = Model_signal.get_signal()

        measurements = [measure_scheme, signal(measure_scheme, self.amplitude, self.frequency, self.phase, self.offset)]

        measurements = Noisifier.noisify(measurements)

        return measurements
    
    def set_frequency(self, freq):

        self.frequency = freq

    def get_frequency(self):

        return self.frequency
    
    def set_phase(self, phase):

        self.frequency = phase
    
    def get_phase(self):

        return self.frequency
    
    def set_amplitude(self, amp):

        self.amplitude = amp

    def get_amplitude(self):

        return self.amplitude
      
    def set_offset(self, off):

        self.offset = off

    def get_offset(self):

        return self.offset

class Noisifier:
    """
    Applies a set noise to a set of measurements to change the noise 
    level use set_noise_level
    """
    def __innit__(self):

        self.noise_level = 0

    def set_noise_level(self, noise):

        self.noise_level = noise

    def get_noise_level(self):

        return self.noise_level

    def noisify(self, measurements : list) -> list:
        """
        This function takes in a set of data points and applies a normal
        distribution of random noise

        Args:
            measurements : list of measurements including x and y values

        Returns:
            list: list of amplitudes with the noise applied 
        """
        times = measurements[0]
        amps = measurements[1]

        noise = np.random.normal(-self.noise_level, self.noise_level, len(times))
        noisy_amps = np.empty_like(amps)
        for i, j in zip(noise, range(len(amps))):
            noisy_amps[j] = i + amps[j]

        return noisy_amps
    
class Model_signal:
    """
    Function to generate the model signal to change it use set_signal 
    giving it a function by which to generate the signal
    """
    def __innit__(self):
        self.function = sin_func

    def set_signal(self, func):

        self.function = func
    
    def get_signal(self):

        return self.function


class Measurement_scheme:
    """
    Scheme by which measurements are made to change pass an array of 
    measurement points to set_scheme
    """
    def __innit__(self):
        self.scheme = np.linspace(0, 5, 50)

    def set_scheme(self, func):
        self.scheme = func

    def get_scheme(self):

        return self.scheme


class Measurement_system:

    def measure():
        return Signal.get_measurements()
    

print(Measurement_system.measure())
import numpy as np

class Wave:
    """
    A object containing all of the necessary data of a sine wave
    """
    def __init__(self, freq: float, phase: float, amp: float, offset: float, time: float, noise_level : float):
        """
        Args:
            freq (float): Frequency
            phase (float): Phase
            amp (float): amplitude
            offset (float): amplitude offset
            time (float): time for which the wave propagates
            noise_level (float): noise level in same measurement as amplitudes
        """
        self.frequency = freq
        self.phase = phase
        self.amp = amp
        self.offset = offset
        self.times = np.arange(0, time, 0.002) #time of propagation
        self.clean_sine_data = (amp * np.sin(self.times * 2 * np.pi* freq + phase)) + offset
        self.noise_level = noise_level
        self.noisy_sine_data = self.noisifier(self.times, self.clean_sine_data, noise_level)

    def noisifier(self, times : list[float], amps:list[float], noise_level) -> list:
        """
        This function takes in a clean sine wave and applies a normal distribution of noise

        Args:
            times (list[float]): List of x values
            amps (list[float]): list of y values
            noise_level (_type_): amplitude of the noise to be applied

        Returns:
            list: list of amplitudes with the noise applied 
        """
        noise = np.random.normal(-noise_level, noise_level, len(times))
        noisy_amps = np.empty_like(amps)
        for i, j in zip(noise, range(len(amps))):
            noisy_amps[j] = i + amps[j]

        return noisy_amps
    
def sin_func( time:list[float], amp: float, freq: float, phase: float, offset: float):
    return amp* np.sin(time * +2 * np.pi * freq + phase) + offset
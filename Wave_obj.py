import numpy as np

class Wave:
    def __init__(self, freq: float, phase: float, amp: float, offset: float, time: float, noise_level : float):
        self.frequency = freq
        self.phase = phase
        self.amp = amp
        self.offset = offset
        self.times = np.arange(0, time, 0.002) #time of propagation
        self.clean_sine_data = (amp * np.sin(self.times * 2 * np.pi* freq + phase)) + offset
        self.noise_level = noise_level
        self.noisy_sine_data = self.noisifier(self.times, self.clean_sine_data, noise_level)

    def noisifier(self, times : list[float], amps:list[float], noise_level):
        noise = np.random.normal(-noise_level, noise_level, len(times))
        noisy_amps = np.empty_like(amps)
        for i, j in zip(noise, range(len(amps))):
            noisy_amps[j] = i + amps[j]

        return noisy_amps
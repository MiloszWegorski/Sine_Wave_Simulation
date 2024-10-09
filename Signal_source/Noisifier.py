import numpy as np

class Noisifier:
    """
    Applies a set noise to a set of measurements to change the noise 
    level use set_noise_level
    """

    noise_level = 0

    @classmethod
    def set_noise_level(cls, noise):
        """
        This Function sets the noise level of the measurements as an
        absolute value

        Args:
            noise (float): level of noise in simulated data
        """

        cls.noise_level = noise

    @classmethod
    def get_noise_level(cls):
        """
        This Function returns the noise level of the measurements as an
        absolute value

        Args:
            noise (float): level of noise in simulated data
        """
        return cls.noise_level

    @classmethod
    def noisify(cls, measurements : list) -> list:
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

        noise = np.random.normal(-cls.noise_level, cls.noise_level, len(times))
        noisy_amps = np.empty_like(amps)
        for i, j in zip(noise, range(len(amps))):
            noisy_amps[j] = i + amps[j]

        return noisy_amps
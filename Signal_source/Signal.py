import numpy as np
from Signal_source.Model_signal import Model_signal
from Signal_source.Noisifier import Noisifier
from Signal_source.Measurement_scheme import Measurement_scheme


class Signal:
    """
    Object which generates Signal measurement points according to the 
    signal and measurement scheme with applied noise from the noisifier
    objects to change these call their respective setters
    """

    frequency = 0.3

    phase = 0
        
    amplitude = 1

    offset = 0


    def get_measurements(self):
        """
        takes a set of 'measurements' from a signal

        Returns:
            List: List of amplitude measurements
        """

        #gets measurement scheme as array of times at which each 
        #measurement was taken
        measure_scheme = Measurement_scheme().get_scheme()

        #gets signal as a function
        signal = Model_signal().get_signal()

        #calculate set of amplitudes for each measurement
        measurements = [measure_scheme, signal(measure_scheme, 
                                               self.amplitude, 
                                               self.frequency, 
                                               self.phase, self.offset)]

        measurements = Noisifier().noisify(measurements)

        return measurements
    
    @classmethod
    def set_frequency(self, freq):
        """
        This function sets the frequency of the incoming signal

        Args:
            freq (Float): Frequency of dignal
        """
        self.frequency = freq

    @classmethod
    def get_frequency(self):
        """
        This function returns the frequency of the incoming signal

        Returns:
            freq (Float): Frequency of dignal
        """
        return self.frequency
    
    @classmethod
    def set_phase(self, phase):
        """
        This function sets the Phase of the incoming signal

        Args:
            Phase (Float): Phase of dignal
        """
        self.frequency = phase
    
    @classmethod
    def get_phase(self):
        """
        This function returns the phase of the incoming signal

        Returns:
            phase (Float): phase of dignal
        """
        return self.frequency
    
    @classmethod
    def set_amplitude(self, amp):
        """
        This function sets the amplitude of the incoming signal

        Args:
            amplitude (Float): amplitude of dignal
        """
        self.amplitude = amp

    @classmethod
    def get_amplitude(self):
        """
        This function returns the amplitude of the incoming signal

        Returns:
            amplitude (Float): amplitude of dignal
        """
        return self.amplitude
      
    @classmethod
    def set_offset(self, off):
        """
        This function sets the offset of the incoming signal

        Args:
            offset (Float): offset of dignal
        """
        self.offset = off

    @classmethod
    def get_offset(self):
        """
        This function returns the offset of the incoming signal

        Returns:
            offset (Float): offset of dignal
        """
        return self.offset


class Measurement_system:

    def measure():
        return Signal().get_measurements()
    


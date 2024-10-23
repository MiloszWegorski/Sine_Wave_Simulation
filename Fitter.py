import numpy as np
import scipy
from abc import ABC, abstractmethod


class fitter(ABC):

    def fit_points(self):
        return self._fit_points()
    
    @abstractmethod
    def _fit_points(self):
        pass


    def get_name(self):
        return self._get_name()
    
    @abstractmethod
    def _get_name():
        pass


class valley_fitter(fitter):

    def __init__(self, threshhold : float, points : np.array):

        self.threshhold = threshhold
        self.times = points[0]
        self.amplitudes = points[1]


    def _fit_points(self):
        


        #calculate the minimum and maximum
        min_amp = np.min(self.amplitudes)
        max_amp = np.max(self.amplitudes)

        #get amplitude
        amplitude = (max_amp - min_amp)/2

        #get offset
        offset = (min_amp + max_amp)/2

        amps_abs = np.abs(self.amplitudes - offset)

        dips = amps_abs < (self.threshhold * amplitude)

        Clump_mask = np.ma.masked_array(np.zeros_like(dips))

        Clump_mask[dips] = np.ma.masked

        Clumps = np.ma.clump_masked(Clump_mask)

        averages = []
        for i in Clumps:
            averages.append(np.average(self.times[i]))

        half_period = np.average(np.diff(averages))

        freq = 1/ (2* half_period)

        #phase
        delta_t = averages[0]

        index_peak = np.int32((Clumps[0].stop + Clumps[1].start)/2)

        if (self.amplitudes[index_peak]- offset) < 0:
            #take delta_t and return phase
            phase = ((delta_t/half_period)*np.pi)
        
        elif (self.amplitudes[index_peak] - offset) > 0:
            
            phase = (((delta_t/half_period)+1)*np.pi)

        return freq,amplitude, offset, phase
    

    def _get_name():
        pass
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
        
        amps_abs = abs(self.amplitudes)


        #calculate the minimum and maximum
        minima = min(self.amplitudes)
        maxima = max(self.amplitudes)

        #get amplitude
        amplitude = (maxima - minima)/2

        #get offset
        offset = np.average([minima + amplitude,
                             maxima - amplitude])
        
        #array to store the values which are below the threshold
        dips = []

        #obtain all values below threshold
        for i, j in zip(self.times, amps_abs):

            if j < self.threshhold*amplitude:
                dips.append(i)

        
        prev = dips[0]
        #array to store biggest x axis gap found
        big = 0

        #find biggest x axis gap between points
        for i in range(1, len(dips)):

            diff = dips[i] - prev

            if diff > big:
                big = diff

            prev = dips[i]

        #array to store the averages
        averages = [0]
        #store total of all previous points
        tot = dips[0]
        #keep count of points
        count = 1

        for i in range(1, len(dips)):
            #if the x axis gap between points is small enough add them
            if (dips[i] - dips[i-1]) < (0.7 * big):
                count += 1
                tot += dips[i]

            #when the gap is bigger means that it belongs to the next
            #half of the waveform therefore average previous sum and 
            #reset the counter
            else:
                averages.append(tot/count)
                tot = dips[i]
                count = 1

        #calculating the length of the gaps between the points 
        gaps = []
        for i in range(1,len(averages)):
            
            gaps.append((averages[i] - averages[i-1]))

        #remove 0th term as it is very small and erroneous
        gaps.pop(0)
        
        #calculate frequency
        freq = 1/ (2* np.average(gaps))

        return amplitude, freq, offset
    
    def _get_name():
        pass
import numpy as np
import scipy

def fit_sin(measurements : list):
    minima = min(measurements[1])
    maxima = max(measurements[1])

    amplitude = (maxima + abs(minima))/2

    offset = maxima - amplitude

    peaks = []

    for i in range(len(measurements[0])- 2):

        if abs(measurements[1][i]) >= abs(measurements[1][i+1]) and abs(measurements[1][i-1]) <= abs(measurements[1][i]):
            
            peaks.append(measurements[0][i])
            peaks.append((measurements[0][i-1] + measurements[0][i+1])/2)

    intervals = []

    for i in range(len(peaks)-2):
        intervals.append(peaks[i+2] - peaks[i])

    interval = 2*np.average(intervals)

    freq = 1/interval

    return freq, amplitude, offset, peaks
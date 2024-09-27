import numpy
import scipy

def fit_sin(measurements : list):
    minima = min(measurements[1])
    maxima = max(measurements[1])

    amplitude = (maxima + abs(minima))/2

    offset = maxima - amplitude

    peaks = []
    print(measurements)
    for i in range(len(measurements[0])- 2):

        if abs(measurements[1][i]) >= abs(measurements[1][i+1]):
            peaks.append((measurements[0][i] + measurements[0][i+1])/2)

    
    interval = 2 * (peaks[1] - peaks[0])

    lam = 1/interval

    return lam, amplitude, offset
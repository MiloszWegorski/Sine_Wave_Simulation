import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from Signal_source.Measurement_schemes import Uniform_Measurement
from Signal_source.Model_signals import Sine_wave
from Signal_source.Measurement_Systems import Measure_Normal_Sine
from Signal_source.Noisifiers import Gaussian_noise
from Fitter import valley_fitter

from Monte_carlo import Monte_carlo_Analyse

def Sine_wav(times, freq, amp, offset, phase):

    return amp * np.sin(2 * times * np.pi * freq + phase) + offset

def simulate_measurement(source_frequency : float, source_amplitude : float, 
         source_phase : float, source_offset : float, threshold : float,
         noise_level : float,start_time : float, end_time : float,
         num_points : int):

    scheme = Uniform_Measurement(start_time, end_time, num_points)

    signal = Sine_wave(source_frequency, source_amplitude, source_phase, 
                    source_offset)

    noisifier_amp = Gaussian_noise(noise_level)
    noisifier_time = Gaussian_noise(noise_level)

    measure_device = Measure_Normal_Sine(scheme, signal)

    points = measure_device.Measure()

    points[1] = noisifier_amp.noisify(points[1])
    points[0] = noisifier_time.noisify(points[0])

    fitter = valley_fitter(threshold, points)

    fitted_freq, fitted_amp, fitted_offset, fitted_phase = fitter.fit_points()

    popt, pcov = curve_fit(Sine_wav, points[0], points[1], 
                             p0=(fitted_freq, fitted_amp, fitted_offset, 
                                 fitted_phase), maxfev=int(1e3))

    return popt[0], popt[1], popt[2], popt[3]


monte_carlo = Monte_carlo_Analyse(simulate_measurement)

monte_carlo.analyse(10000)

#print('amplitude : ' + str(a))
#print('frequency : ' + str(f))
#print('offset: ' + str(o))
#print('Phase: ' + str(p))

#measured_signal = Sine_wave(f, a, p, o)

#measured_scheme = Uniform_Measurement(0, 2, 1000)

#measure_device_out = Measure_Normal_Sine(measured_scheme, measured_signal)

#measured_points = measure_device_out.Measure()

#plt.scatter(points[0], points[1], label = 'measurement points')
#plt.plot(measured_points[0], measured_points[1], label='fitted signal', color = 'r')
#plt.axhline(threshold)
#plt.legend()
#plt.show()
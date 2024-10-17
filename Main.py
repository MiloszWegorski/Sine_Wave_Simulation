import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from Signal_source.Measurement_schemes import Uniform_Measurement
from Signal_source.Model_signals import Sine_wave
from Signal_source.Measurement_Systems import Measure_Normal_Sine
from Signal_source.Noisifiers import Gaussian_noise
from Fitter import valley_fitter

scheme = Uniform_Measurement(0, 2, 200)

signal = Sine_wave(2, 1, 0, 0)

noisifier_amp = Gaussian_noise(0.05)
noisifier_time = Gaussian_noise(0)

measure_device = Measure_Normal_Sine(scheme, signal)

points = measure_device.Measure()

points[1] = noisifier_amp.noisify(points[1])
points[0] = noisifier_time.noisify(points[0])

threshold = 0.5




fitter = valley_fitter(threshold, points)

a, f, o = fitter.fit_points()
print('amplitude : ' + str(a))
print('frequency : ' + str(f))

measured_signal = Sine_wave(f, a, o, 0)

measured_scheme = Uniform_Measurement(0, 2, 1000)

measure_device_out = Measure_Normal_Sine(measured_scheme, measured_signal)

measured_points = measure_device_out.Measure()

plt.scatter(points[0], points[1], label = 'measurement points')
plt.plot(measured_points[0], measured_points[1], label='fitted signal', color = 'r')
plt.legend()
plt.show()
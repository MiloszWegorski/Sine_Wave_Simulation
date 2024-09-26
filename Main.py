from scipy.optimize import curve_fit
from Wave_obj import Wave, sin_func
import matplotlib.pyplot as plt
from Measurer import measure
import numpy as np

#generating test wave
wav1 = Wave(freq=5, phase=0.5, amp=1, offset=0.25, time=3, noise_level=0.2)

print()

fig, ax = plt.subplots(2,2)

#plotting the data
ax[0][0].plot(wav1.times, wav1.clean_sine_data)
ax[0][1].plot(wav1.times, wav1.noisy_sine_data)

#getting test measurements
results = measure(6, 0.07, wav1.clean_sine_data, wav1.times)
results_noise = measure(6, 0.07, wav1.noisy_sine_data, wav1.times)

#plotting measurements
ax[0][0].scatter(results[0], results[1], color = 'r')
ax[0][1].scatter(results_noise[0], results_noise[1], color = 'r')

ax[1][0].scatter(results[0], results[1], color = 'r')
ax[1][1].scatter(results_noise[0], results_noise[1], color = 'r')

ax[0][0].set_xlabel('time')
ax[0][0].set_ylabel('Amplitude')

ax[0][1].set_xlabel('time')
ax[0][1].set_ylabel('Amplitude')

ax[0][0].grid()
ax[0][1].grid()

ax[1][0].grid()
ax[1][1].grid()

popt, pcov = curve_fit(sin_func, results_noise[0], 
                       results_noise[1] ,p0=(1, 3, 0.2, 0)
                       , maxfev=int(1000))



time_vals = wav1.times

a, f, p , o = popt

matched_data = (a * np.sin(time_vals * 2 * np.pi* f + p)) + o

ax[1][1].plot(time_vals, matched_data)

print(popt)
plt.show()

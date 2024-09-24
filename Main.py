from Wave_obj import Wave
import matplotlib.pyplot as plt
from Measurer import measure

wav1 = Wave(5, 0.5, 1, 0.25, 3, 0.02)

print()

fig, ax = plt.subplots(1,2)

#ax[0].plot(wav1.times, wav1.clean_sine_data)ax[1].plot(wav1.times, wav1.noisy_sine_data)


results = measure(6, 0.37, wav1.clean_sine_data, wav1.times)
results_noise = measure(6, 0.37, wav1.noisy_sine_data, wav1.times)

ax[0].scatter(results[0], results[1], color = 'r')
ax[1].scatter(results_noise[0], results_noise[1], color = 'r')

ax[0].set_xlabel('time')
ax[0].set_ylabel('Amplitude')

ax[1].set_xlabel('time')
ax[1].set_ylabel('Amplitude')

ax[0].grid()
ax[1].grid()

plt.show()

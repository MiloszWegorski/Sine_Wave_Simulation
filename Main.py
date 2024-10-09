import numpy as np
import matplotlib.pyplot as plt
import random

from prediction_algorithm import fit_sin
from Signal_source.Signal import Measurement_system
from Signal_source.Model_signal import Model_signal, sin_func
from Signal_source.Noisifier import Noisifier
from Signal_source.Measurement_scheme import Measurement_scheme

arr = []
tot = 0

for i in range(50):
    arr.append(float(tot))
    tot = tot + random.uniform(0, 0.7)

Measurement_scheme().set_scheme(arr)

signal = Measurement_system.measure()

measurements = [Measurement_scheme().get_scheme(), signal]

freq, amp, off, peaks = fit_sin(measurements)

time = np.linspace(0, arr[-1], 1000)

plt.plot(time, sin_func(time, amp, freq, 0, off))

plt.scatter(Measurement_scheme().get_scheme(), signal)
plt.show()
import numpy as np
import matplotlib.pyplot as plt


from Signal_source.Measurement_schemes import UniformMeasurement, LogMeasurement
from Signal_source.Model_signals import ModelSineSignal, NoisySignal
from Signal_source.Measurement_Systems import MeasurementSystem
from Fitter import ValleyFitter, low_pass_filter, Sine_wav

from Monte_carlo import MonteCarloAnalyse


def sweep_variable(num_trails:int ,scheme , model_signal,
                fitter, value_range:tuple, sweep_variable):


    sweep_range = np.linspace(value_range[0], value_range[1], value_range[2])

    freq_std = []
    amp_std = []
    offset_std = []
    phase_std = []

    measure_device = MeasurementSystem(scheme, signal)
    
    for i in sweep_range:

        measure_device.set_param_value(sweep_variable, i)

        measure_device = MeasurementSystem(scheme, signal)
        
        results = monte_carlo.simulate(num_trails, measure_device, fitter)
    
        freq_std.append(np.std(results.freq_results))
        amp_std.append(np.std(results.amp_results))
        offset_std.append(np.std(results.offset_results))
        phase_std.append(np.std(results.phase_results))

    fig2, ax2 = plt.subplots(2, 2)

    for i in ax2:
        for j in i:
            j.set_xlabel('Noise level')
            j.set_ylabel('Standard Deviation')

    
    ax2[0][0].set_title('Frequency')
    ax2[0][0].plot(sweep_range, freq_std)
    ax2[0][1].set_title('Amplitude')
    ax2[0][1].plot(sweep_range, amp_std)
    ax2[1][0].set_title('Offset')
    ax2[1][0].plot(sweep_range, offset_std)
    ax2[1][1].set_title('Phase')
    ax2[1][1].plot(sweep_range, phase_std)

    plt.show()

start_time = 0
end_time = 5
num_points = 100

scheme = UniformMeasurement(start_time, end_time, num_points)

source_frequency = 2
source_amplitude = 1
source_phase = 0
source_offset = 0.2

model_signal = ModelSineSignal(source_frequency, source_amplitude, source_phase, 
                source_offset)

system = MeasurementSystem(scheme, model_signal)

threshold = 0.6
fitter = ValleyFitter(threshold)

monte_carlo = MonteCarloAnalyse()

signal = NoisySignal(model_signal, 0.1)

sweep_variable(500, scheme, signal, fitter, (0, 1e-2, 10), 'noise level') 

"""
#noise_sweep(500, scheme, model_signal, fitter, (0, 1e-2, 5))

data_density_sweep((70, 500, 50), model_signal, fitter, 100, 0, 5)


device = MeasurementSystem(scheme, signal)

data = device.Measure()

results = fitter.fit_points(data)

x_vals = np.linspace(0, 5, 1000)

print(f'frequency = {results[0]}')
print(f'Amplitude = {results[1]}')

plt.plot(x_vals, Sine_wav(x_vals,*results))
plt.scatter(data[0], data[1])

plt.show()
"""
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class Analysis(ABC):

    def analyse(self, num_trails):
        self._analyze(num_trails)

    @abstractmethod
    def _analyze(num_trails):
        pass


class Monte_carlo_Analyse(Analysis):

    def __init__(self, func):
        self.func = func


    def _analyze(self, num_trails):
        
        freq_results = []
        amp_results = []
        offset_results = []
        phase_results = []

        freq = 2
        amp = 1
        phase = 0.25
        off = 0.2
        thresh = 0.35
        noise_level = 0.05
        start = 0
        end = 2
        num = 200


        for i in range(num_trails):
            freq_fit, amp_fit, off_fit, phase_fit = self.func(freq, amp, phase,
                                                              off, thresh,
                                                              noise_level, start,
                                                              end, num)
            
            freq_results.append(freq_fit)
            amp_results.append(amp_fit)
            offset_results.append(off_fit)
            phase_results.append(phase_fit)

        freq_std = np.std(freq_results)
        print('Frequency Standard deviation : ' + str(freq_std))

        amp_std = np.std(amp_results)
        print('Amplitude Standard deviation : ' + str(amp_std))

        offset_std = np.std(offset_results)
        print('offset Standard deviation : ' + str(offset_std))
        
        phase_std = np.std(phase_results)
        print('Phase Standard deviation : ' + str(phase_std))

        fig, ax = plt.subplots(2, 2)

        ax[0][0].set_title('Frequency')
        ax[0][0].hist(freq_results, bins = 100)
        ax[0][0].axvline(freq, color='r', linestyle='--')

        ax[0][1].set_title('Amplitude')
        ax[0][1].hist(amp_results, bins = 100)
        ax[0][1].axvline(amp, color='r', linestyle='--')

        ax[1][0].set_title('offset')
        ax[1][0].hist(offset_results, bins = 100)
        ax[1][0].axvline(off, color='r', linestyle='--')

        ax[1][1].set_title('phase')
        ax[1][1].hist(phase_results, bins = 100)
        ax[1][1].axvline(phase, color='r', linestyle='--')

        plt.show()
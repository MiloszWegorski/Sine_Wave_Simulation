class MonteCarloAnalyse():

    def __init__(self):
        self.freq_results = []
        self.amp_results = []
        self.offset_results = []
        self.phase_results = []


    def simulate(self, num_trails, measure_device, fitter):

        for i in range(num_trails):

            data = measure_device.Measure()
            
            popt = fitter.fit_points(data)

            
            self.freq_results.append(popt[0])
            self.amp_results.append(popt[1])
            self.offset_results.append(popt[2])
            self.phase_results.append(popt[3])

        
        return self
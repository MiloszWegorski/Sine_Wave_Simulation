import numpy as np
from scipy import stats
from abc import ABC, abstractmethod

class Measurement_scheme(ABC):
    
    def get_points(self):
        return self._get_points()
    
    @abstractmethod
    def _get_points(self):
        pass
    
    def get_name(self):
        return self._get_name()
    
    @abstractmethod
    def _get_name(self):
        pass

class Uniform_Measurement(Measurement_scheme):

    def __init__(self, start, end, num_points):
        self.start = start
        self.end = end
        self.num_points = num_points

        self.name = f"Uniform distribution from {start} to {end} with {num_points} points"

    def _get_points(self):
        return np.array(np.linspace(self.start, self.end, self.num_points))
    
    def _get_name(self):
        return self.name
    

class Log_Measurement(Measurement_scheme):

    def __init__(self, start, end, num_points):
        self.start = start
        self.end = end
        self.num_points = num_points

        self.name = f"Logarithmic distribution from {start} to {end} with {num_points} points"

    def _get_points(self):
        return np.logspace(self.start, self.end, self.num_points)
    
    def get_name(self):
        return self.name
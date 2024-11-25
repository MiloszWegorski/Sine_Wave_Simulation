import numpy as np
class MeasurementSystem():
    """_summary_
    """
    def __init__(self, scheme, signal):
        """_summary_

        Args:
            scheme (Measurement Scheme): _description_
            signal (Signal): _description_
        """
        self.scheme = scheme
        self.signal = signal

    
    def Measure(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        times = self.scheme.get_points()
        
        return [np.array(times), np.array(self.signal.get_amplitudes(times))]
        #add get variables method
    
    def get_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f'I measure a normal sine wave'
    
    def get_param_value(self, param_name):
        match param_name:
            case 'start_time' | 'end_time' | 'num_points':
                return self.scheme.get_param_value(param_name)
            case 'frequency' | 'amplitude' | 'phase' | 'offset':
                return self.signal.get_param_value(param_name)
            case _:
                raise ValueError(f'Unknown parameter name : {param_name}')
            
    def set_param_value(self, param_name, value):
        match param_name:
            case 'start_time' | 'end_time' | 'num_points':
                return self.scheme.set_param_value(param_name, value)
            case 'frequency' | 'amplitude' | 'phase' | 'offset' | 'noise level':
                return self.signal.set_param_value(param_name, value)
            case _:
                raise ValueError(f'Unknown parameter name : {param_name}')
            
    def get_param_names(self):
        param_names = self.signal.get_param_names() + self.scheme.get_param_names()

        return param_names
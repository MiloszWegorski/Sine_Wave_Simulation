import numpy as np

class Measurement_scheme:
    """
    Scheme by which measurements are made to change pass an array of 
    measurement points to set_scheme
    """
    
    scheme = np.linspace(0, 1, 11)

    @classmethod
    def set_scheme(cls, func):
        """This function changes the measurement scheme used

        Args:
            func (List): list of measurement times
        """
        cls.scheme = func
    
    @classmethod
    def get_scheme(cls):
        """Returns the current measurement scheme in use

        Returns:
            List: list of times at which measurements are taken 
        """

        return cls.scheme
import numpy as np

def sin_func(time:list[float], amp: float, freq: float, phase: float, offset: float):
    """
    

    Args:
        time (list[float]): _description_
        amp (float): _description_
        freq (float): _description_
        phase (float): _description_
        offset (float): _description_

    Returns:
        _type_: _description_
    """
    if type(time) is list:
        time = np.array(time)

    return amp * np.sin(2 * time * np.pi * freq + phase) + offset

class Model_signal:
    """
    Function to generate the model signal to change it use set_signal 
    giving it a function by which to generate the signal
    """

    function = sin_func

    @classmethod
    def set_signal(cls, func):
        """Used to set the function by which the signal  is generated

        Args:
            func (): _description_
        """

        cls.function = func


    @classmethod
    def get_signal(cls):
        """Returns the function by which the model signal is generated

        Returns:
            Function: function to generate model signal 
        """
        return cls.function

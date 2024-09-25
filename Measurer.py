def measure(num_measurements : int, interval:float, wave_data : list[float], times : list[float]) -> list: 
    """
    This function creates 'measurements' with specific increments on the x axis

    Args:
        num_measurements (int): Total number of measurements to be taken
        interval (float): Interval on the X axis with which the measurements are to be taken
        wave_data (list[float]): Y axis values
        times (list[float]): x axis values

    Returns:
        list: 2d array where [[x values of each measurement][y values of each measurement]]
    """
    counter = 0
    out = [[], []]

    for i in range(len(times)):
        if num_measurements != 0:
            if (interval * counter) < times[i]:
                out[0].append(times[i - 1])
                out[1].append(wave_data[i - 1])
                counter += 1
                num_measurements -= 1

    
    return out
def measure(num_measurements : int, interval:float, wave_data : list[float], times : list[float]) -> list: 

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
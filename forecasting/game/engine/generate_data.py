import numpy as np
import pandas as pd
import datetime
from game.models import EASY, NORMAL, HARD

def generate_data(difficulty: str, length: int = 365, highest_amplitude: float = 10.0, start_value: float = 100):
    data_array = np.full(shape=length, fill_value=start_value)
    prediction_array = np.zeros(shape=length)
    start_date = datetime.datetime.today().date() - datetime.timedelta(days=int(length/2))

    date_array = pd.date_range(start=start_date, periods=length)

    # easy 
    #if difficulty == EASY:


    data = pd.DataFrame({'Values':data_array, 'Predictions':prediction_array}, index=date_array)

    return data



def _generate_simple_trend(total_length: int = 0, start: float = 0.0, stop: float = 100.0) -> np.ndarray:
    data = np.arange(start = start,stop = stop, step = (stop-start)/total_length)
    if len(data) > total_length:
        data = data[:total_length]
    return data

def _generate_seasonality(option: str = "", total_length: int = 0, inverse_frequency: float = 1.0, amplitude: float = 0.0):
    if option in ["weekly", "daily", "monthly", "season", "yearly"]:
        match option:
            case "weekly":
                frequency = int(total_length / 7)
            case "daily":
                frequency = int(total_length)
            case "monthly":
                frequency = int(total_length / 30)
            case "yearly":
                frequency = int(total_length / 365)
            case "season":
                frequency = int(total_length / 91)
    else:
        frequency = inverse_frequency

    x = np.arange(0, total_length)
    return -amplitude*np.cos((2*np.pi)*x/(total_length/frequency))

def _generate_noise(total_length: int = 0, noise_mean: float = 0.0, noise_std: float = 1.0):
    return np.random.normal(noise_mean, noise_std, total_length)

def _generate_random_mask(total_length: int = 0, mask_probability: float = 0.0):
    return np.random.choice([True, False], size=total_length, p=[mask_probability, 1-mask_probability])
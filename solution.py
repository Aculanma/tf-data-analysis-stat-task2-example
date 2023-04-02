import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1099254596 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return np.mean(x) + np.std(x) * norm.ppf(alpha / 2) / np.sqrt(len(x)), \
           np.mean(x) + np.std(x) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))

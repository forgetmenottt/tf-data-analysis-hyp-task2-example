import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 1372197133 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p_value = ks_2samp(x, y, alternative="two-sided").pvalue
    alpha = 0.05

    if (p_value < alpha):
        a = True
    else:
        a = False
    return a # Ваш ответ, True или False

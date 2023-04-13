import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.02
    success = np.array([x_success, y_success])
    cnt = np.array([x_cnt, y_cnt])
    stat, p_value = proportions_ztest(count = success, nobs = cnt, alternative='smaller')
    if p_value < alpha:
        return True
    else:
        return False

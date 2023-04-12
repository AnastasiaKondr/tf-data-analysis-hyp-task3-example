import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 483660375 # Ваш chat ID, не меняйте название переменной


def solution(X, Y) -> bool:
    alpha = 0.05
    # Проверяем равенство дисперсий выборок
    var_X = np.var(X)
    var_Y = np.var(Y)
    if var_X == var_Y:
        equal_var = True
    else:
        equal_var = False

    # Выполняем t-тест
    t_stat, p_val = ttest_ind(X, Y, equal_var=equal_var)

    # Сравниваем p-значение с уровнем значимости
    if p_val < alpha:
        return True  # Отклоняем нулевую гипотезу
    else:
        return False  # Не отклоняем нулевую гипотезу
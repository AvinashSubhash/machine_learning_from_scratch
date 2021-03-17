import numpy as np
import random

def data_creator(size,noise=5):
    data = np.zeros((2,size))
    for i in range(size):
        data[0][i] = i
        if i >= 2*(size/noise) and i <= 3*(size/noise):
            if random.randint(1,100) > 65:
                data[1][i] = 0
            else:
                data[1][i] = 1
        elif i < 2*(size/noise):
            data[1][i] = 1
        else:
            data[1][i] = 0
    return data


def analyser(data):
    

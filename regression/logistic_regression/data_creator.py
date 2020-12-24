import numpy as np
import random
def creator(perc1):
    data = np.ones((5000,2))
    flag = 0
    for i in range(5000):
        if flag == 0:
            data[i][0] = random.uniform(0.1,6.2)
            data[i][1] = random.uniform(0.1,4.1)
            flag = 1
        elif flag == 1:
            data[i][0] = random.uniform(7.1,13.2)
            data[i][1] = random.uniform(6.1,10.1)
            flag = 0
        #print(data[i],"\n")
    return data
    #print(data)

#creator(55)
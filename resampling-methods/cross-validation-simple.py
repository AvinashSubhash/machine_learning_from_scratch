# Simple Liiinear regression with validation set.
import data_creator
import numpy as np
weight = 0
bias = 0

data = data_creator.creator(55)
np.random.shuffle(data)
train_data = data[0:4000]
print("Training data size: ",train_data.shape)
test_data = data[4000:]
print("Test data size: ",test_data.shape)

result = test_data
sum = np.sum(train_data,axis=0)
sum = sum/4000

weight_upper = 0
weight_lower= 0
difference = 0
for i in range(4000):
    weight_upper += (train_data[i][0]-sum[0])*(train_data[i][1]-sum[1])
    weight_lower += (train_data[i][0]-sum[0])*(train_data[i][0]-sum[0])

weight = weight_upper/weight_lower
bias = sum[1] - (weight*sum[0])
for i in result:
    #print("Expected: ",i[1]," Calculated: ",(weight*i[0])+bias)
    difference += (i[0]-((weight*i[0])+bias))
difference = difference/1000
print("Mean Error: ",difference)


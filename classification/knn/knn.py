from math import sqrt

def distance_calc(row_1,row_2):
    distance = 0.0
    for i in range(len(row_1)-1):
        distance += (row_1[i]-row_2[i])**2
    return sqrt(distance)

def nearest_1(train_data,test_data,neighbours):
    distances = list()
    for train_row in train_data:
        distance1 = distance_calc(test_data,train_row)
        distances.append((train_row,distance1))
    distances.sort(key = lambda tuple1: tuple1[1])
    neighbour_list = list()
    for i in range(neighbours):
        neighbour_list.append(distances[i][0])
    return neighbour_list

def knn_predictor(train_data,test_data,neighbours):
    neighbours_list = nearest_1(train_data,test_data,neighbours)
    values = [data[-1] for data on neighbours_list]
    prediction = max(set(values),key=values.count)
    return prediction




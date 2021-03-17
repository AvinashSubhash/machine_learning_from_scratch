#basic classification program
import data_creator
import numpy as np

def modifier(data):

    for i in data:
        print((1/(1+pow(2.718,-i[1]))))
        if (1/(1+pow(2.718,-i[1]))) > 0.5:
            i[1] = 1
        else:
            i[1] = 0
    return data

weight = 0
bias = 0

data = data_creator.creator(55)
result = np.copy(data)


sum = np.sum(data,axis=0)
sum = sum/5000


weight_upper = 0
weight_lower = 0
for i in range(5000):
    weight_upper += (data[i][0]-sum[0])*(data[i][1]-sum[1])
    weight_lower += (data[i][0]-sum[0])*(data[i][0]-sum[0])

weight = weight_upper/weight_lower

bias = sum[1] - (weight*sum[0])
for i in result:
    i[1] = (weight*i[0])+bias
    #print(i[1])
#print(result)
#result = modifier(result)
print("weight: ",weight,"\n","Bias: ",bias)

error = 0
for i in range(5000):
    #print("data=",data[i][1]," result=",result[i][1])
    if data[i][1] != result[i][1]:
        #print("data: ",data[i][1],", result: ",result[i][1])
        error+=1

#print("No. of errored values: ",error)
while(True):

    test = int(input())
    print("two" if (weight*test)+bias> 4 else "one")
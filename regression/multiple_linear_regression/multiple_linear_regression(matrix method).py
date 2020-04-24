# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:52:36 2020

@author: Aiva
"""

"""Multiple linear regression program with the concept of matrix multiplication and inverse calculation

   This program displays the resultant equation of the data sets given 
   and shows the predicted output from taking sample input"""


import numpy as np
sets=[]
output=[]
no_of_variables=int(input("Enter the number of variables\n"))
no_of_data=int(input("Enter the number of data\n"))
data=np.zeros((no_of_data,no_of_variables+1))
output=np.zeros((no_of_data,1))
data[:,0]=1

for i in range(no_of_data):
    sets=input("Enter the set")
    sets=sets.split(",")
    data[i][1:no_of_variables+1]=sets[0:no_of_variables]
    output[i][0]=sets[no_of_variables]

    
data_transpose=np.zeros((no_of_variables+1,no_of_data))


for i in range(no_of_variables+1):
    for j in range(no_of_data):
        data_transpose[i][j]=data[j][i]
        
data_transpose_data=np.dot(data_transpose,data)

data_transpose_y=np.dot(data_transpose,output)

data_transpose_data=np.linalg.inv(data_transpose_data)

coeffecients=np.dot(data_transpose_data,data_transpose_y)

print(coeffecients)

#Testing data
xcord=input("Enter tha data for prediction").split(",")
xcord.insert(0,1)
for i in range(len(xcord)):
    xcord[i]=int(xcord[i])
    
prediction=np.dot(xcord,coeffecients)
for i in range(len(prediction)):
    prediction[i]=round(prediction[i],5)

print("The predicted output is: ",prediction)
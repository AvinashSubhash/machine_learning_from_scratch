# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:47:44 2020

@author: Aiva
"""

import numpy as np
cords=np.zeros(2)
size=int(input("Enter the number of training data:"))
data=np.zeros((size,2))
mean=[]
for i in range(size):
    cords=input().split(",")
    data[i][0]=int(cords[0])
    data[i][1]=int(cords[1])

mean=(data.sum(axis=0))/size
beta_upper=0
beta_lower=0

for i in range(size):
    beta_upper+=(data[i][0]-mean[0])*(data[i][1]-mean[1])
    beta_lower+=(data[i][0]-mean[0])*(data[i][0]-mean[0])
    
beta_i=(beta_upper/beta_lower)
beta_o=(mean[1]-(beta_i*mean[0])) 

print("resulted equation is y=",beta_i,"x + ",beta_o,"\n")  
    

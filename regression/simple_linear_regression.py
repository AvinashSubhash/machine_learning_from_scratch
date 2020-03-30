# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:47:44 2020

@author: Aiva
"""
"""Simple linear regression program with the concept of reducing the squared errors

   This program displays the resultant equation of the data sets given 
   and shows the accuracy level of the algorithm with respect to the data sets"""
import numpy as np
se_line=0
se_mean=0
accuracy=0
xcord=0
ycord=0
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

for i in range(size):
    se_line+=(data[i][1]-((beta_i*data[i][0])+beta_o))*(data[i][1]-((beta_i*data[i][0])+beta_o))
    se_mean+=(data[i][1]-mean[1])*(data[i][1]-mean[1])
    
accuracy=1-(se_line/se_mean)    

print("The accuracy of the algorithm in this case is: ",accuracy*100,"%")
"""Furthur it takes an input and predicts the output from the data analysis"""
print("Enter the x cordinate data")
xcord=int(input())
ycord=(beta_i*xcord)+beta_o
print("The predicted output is: ",ycord)


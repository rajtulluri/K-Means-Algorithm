import pandas as pd
import numpy as np
import random
import math

def distance(point): #Calculate distance between point and all centroids
    min_dist = 100 #Infinite value to find minimum
    cls = 0
    for k in range(1,K+1):
        dist = 0
        centroid = Classes[k]
        for i,j in zip(centroid,point):
            dist += (i-j)**2 #Euclidean distance
        if(dist < min_dist):
            min_dist = dist
            cls = k
    return cls #returns the cluster, point is associated to

df = pd.read_csv('Iris.csv')
target = df.Species
df = df.drop('Species',axis=1) #Removing labels from the dataset
df.set_index('Id',inplace=True)

K = int(input("Enter number of Clusters "))
#Initializing K classes with random centroid values
Classes = {label: df.iloc[val].values for label,val in 
           zip((i for i in range(1,K+1)),random.sample(range(1,len(df)),K))} 

diff=1 #Initializing to high value
while(diff): #While change in old and new centroid values
    Clusters = dict([(key,[]) for key in Classes.keys()]) #Cluster dictionary with empty list
    tmp = []
    for index in range(0,len(df)):
        pair = distance(df.iloc[index]) #Calculating distance for every point in dataframe
        tmp = Clusters[pair]
        tmp.append(index)
        Clusters[pair] = tmp #Adding index of point to corresponding class
    Mean = []
    for k in Clusters.keys():
        Mean.append(df.iloc[Clusters[k]].mean().values) #Find new centroid values
        
    diff = abs(sum(sum(Classes.values())) - sum(sum(Mean))) #Cumulative difference between old and new Centroid value
    if diff:
        for k in Clusters.keys():
            Classes[k] = Mean[k-1] #Centroid values updated
            
print(Clusters)

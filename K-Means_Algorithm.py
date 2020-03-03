import pandas as pd
import numpy as np
import random
import math

def distance(point,index):
    min_dist = 100
    cls = 0
    for k in range(1,K+1):
        dist = 0
        centroid = Classes[k]
        for i,j in zip(centroid,point):
            dist += (i-j)**2
        if(dist < min_dist):
            min_dist = dist
            cls = k
    return (cls,index)

df = pd.read_csv('Iris.csv')
target = df.Species
df = df.drop('Species',axis=1)
df.set_index('Id',inplace=True)

K = int(input("Enter number of Clusters "))
Classes = {label: df.iloc[val].values for label,val in 
           zip((i for i in range(1,K+1)),random.sample(range(1,len(df)),K))}
diff=1
while(diff > math.exp(-130)):
    Clusters = dict([(key,[]) for key in Classes.keys()])
    tmp = []
    for ind in range(0,len(df)):
        pair = distance(df.iloc[ind],ind)
        tmp = Clusters[pair[0]]
        tmp.append(pair[1])
        Clusters[pair[0]] = tmp
    Mean = []
    for k in Clusters.keys():
        Mean.append(df.iloc[Clusters[k]].mean().values)
        
    diff = abs(sum(sum(Classes.values())) - sum(sum(Mean)))
    if diff > math.exp(-9):
        for k in Clusters.keys():
            Classes[k] = Mean[k-1]
            
print(Clusters)

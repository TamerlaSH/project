import pandas as pd
import numpy as np

Androids = 0
IOS = 0
An = 0
Ioss = 0
plat = pd.read_csv('features_data_with_churned')
platforms = plat["platform"]
for i in platforms:
    if i == "Android":
        Androids+=1
    if i == "iOS":
        IOS+=1

print(Androids)
print(IOS)
print(IOS//Androids)

print("---------------------------------")
print("_________________________________")

chunked = plat["churned"]
chun = 0
for i in range(len(chunked)):
    if chunked[i]==1 and platforms[i]=="Android":
        An+=1
print(An)




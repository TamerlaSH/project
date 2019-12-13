import pandas as pd
import numpy as np

data = pd.read_csv('equity_value_data.csv')
times = data["timestamp"]
user = data["user_id"]
count = []
counts = 0
plat = pd.read_csv('features_data_with_churned')
platform = plat["platform"]
user_id=plat["user_id"]
for i in range(len(user)-2):
    if user[i]==user[i+1]:
        counts+=1
    else:
        count.append((counts, user[i]))
        counts=0
counts_user = [i[0] for i in count]
print(max(counts_user))
print(counts_user.index(max(counts_user)))
print(count[counts_user.index(max(counts_user))])

time_android = 0
time_IOS = 0
for i in range(0, len(counts_user)):
    k = count[i][1]
    ind = user.index(k)
    if platform[ind] == 1:
        time_android+=count[i][0]
    if platform[ind] == -1:
        time_IOS+=count[i][0]

print(time_IOS/time_android)

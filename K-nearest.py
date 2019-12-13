import pandas as pd
from math import sqrt

df = pd.read_csv('features_data_with_normalisations.csv')
size_train = int(len(df) * 0.75)
K = 9
train = df[:size_train]
test = df[size_train:]

def distance(x, y):
    summ = []
    for i in range(len(x)):
        summ.append((x[i] + y[i]) ** 2)
    return sqrt(sum(summ))

def is_churned(user, train):
    neighbours = []
    train_size = len(train['investment_experience'])
    for i in range(train_size):
        line_of_train = list(train.iloc[i])
        neighbours.append((distance(user[:-2],line_of_train[:-2]), line_of_train[-1]))

    k_near = sorted(neighbours, key=lambda x: x[0])
    k_near = k_near[:3]

    count_churn = sum([x[1] for x in k_near])

    if count_churn>K//2:
        return True
    else:
        return False


test_size = len(test["investment_experience"])
right_answer = 0
for i in range(test_size):
    user_data = list(test.iloc[i])
    print(i)
    churned = is_churned(user_data, train)
    if (churned and user_data[-1] == 1) or (not churned and user_data[-1] == 0):
        right_answer += 1

print("right_answer", right_answer)

print("procent right", right_answer/test_size)


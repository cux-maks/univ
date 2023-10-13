import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = load_iris()

total = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], np.float64)
names = ['setosa', 'versicolor', 'virginica']

i = 0

while i < 150:
    total[iris['target'][i]] += iris['data'][i]
    i += 1

total /= 50

for x in range(3):
    print("<{}>".format(names[x]))
    for d in total[x]:
        print("sepal length: {}".format(d))
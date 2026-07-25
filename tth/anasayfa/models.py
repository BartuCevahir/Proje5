from django.db import models

# Create your models here.
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([
    [90, 85, 80, 88],
    [70, 75, 65, 72],
    [95, 92, 91, 94],
    [60, 55, 70, 65],
    [85, 80, 78, 82],
    [50, 45, 60, 55],
])

y = np.array([
    86,
    71,
    93,
    62,
    81,
    52,
])

model = LinearRegression()

model.fit(X, y)
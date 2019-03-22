#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt


whiteNoi = []
randWalk = []

mu, sigma = 0, 0.2 # mean and standard deviation
temp = 0
for i in range(0,20000):
    s = np.random.normal(mu, sigma, 1)
    whiteNoi.append(s[0])
    s = np.random.normal(mu, sigma, 1)
    temp += s[0]
    randWalk.append(temp)

# plt.plot(np.array(whiteNoi)+np.array(randWalk))
# plt.show()

gyroOut = np.array(whiteNoi)+np.array(randWalk)


for i in np.size(gyroOut):
    gyroOutInte = np.sum(gyroOut[0:i])
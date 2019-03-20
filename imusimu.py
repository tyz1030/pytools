#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

whiteNoi = []
randWalk = []

mu, sigma = 0, 0.2 # mean and standard deviation
temp = 0
for i in range(0,2000000):
    s = np.random.normal(mu, sigma, 1)
    whiteNoi.append(s[0])
    s = np.random.normal(mu, sigma, 1)
    temp += s[0]
    randWalk.append(temp)

plt.plot(np.array(whiteNoi)+np.array(randWalk))
plt.show()

ad = []
for tau in range(1,1000000):
    a = np.square((randWalk[0] - 2*randWalk[tau] + randWalk[2*tau]))/(2*tau*tau)
    ad.append(a)

b = np.arange(0,25000-0.025,0.025)

# print(np.shape(b))
plt.plot(b,np.array(ad))
plt.yscale('log')
plt.xscale('log')

plt.show()
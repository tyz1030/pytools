#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import allantools as allan

whiteNoi = []
randWalk = []

mu, sigma = 0, 0.2 # mean and standard deviation
temp = 0
for i in range(0,100000):
    s = np.random.normal(mu, sigma, 1)
    whiteNoi.append(s[0])
    s = np.random.normal(mu, sigma, 1)
    temp += s[0]
    randWalk.append(temp)

gyroOut = np.array(whiteNoi)+np.array(randWalk)

# ad = []
# for tau in range(1,10000):
#     a = np.square((randWalk[0] - 2*randWalk[tau] + randWalk[2*tau]))/(2*tau*tau)
#     ad.append(a)

# b = np.arange(0,250-0.025,0.025)

# # print(np.shape(b))
# plt.plot(b,np.array(ad))
x = allan.noise.white(100000)


# print(x+np.array(randWalk))
plt.plot(x+np.array(randWalk))
plt.show()

for i in range(0,np.size(gyroOut)):
    gyroOutInte = np.sum(gyroOut[0:i])

(taus2, ad, ade, ns) = allan.adev(x+np.array(randWalk),rate=415.0, data_type="phase", taus="all")

print(np.shape(taus2))

plt.plot(ad)
plt.yscale('log')
plt.xscale('log')

plt.show()
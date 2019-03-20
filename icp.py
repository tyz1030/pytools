#!/usr/bin/python

import numpy as np

class icp:
    def __init__(self):
        self.R = np.eye(3, 3)
        self.srcAlign = []

    def runIcp(self, src, dst, iter):
        tempsrc = src.copy()
        generalR = np.eye(3,3)
        for i in range(0,iter):
            nbr = self.findNbr(tempsrc, dst)
            R = self.findRot(tempsrc, nbr)
            generalR = np.matmul(R, generalR)
            tempsrc = np.transpose(np.matmul(generalR, np.asarray(src.copy()).T))
            # tempsrc = tempsrc.tolist()
            print (i)
        return tempsrc, generalR


    def findNbr(self, src, dst):
        tempDst = dst.copy()
        nearestNbrs = []
        for i in range(0, len(list(src))):
            minDist = 10000
            nearestIdx = 0
            for j in range(0, len(list(dst))):
                dist = (tempDst[j,0]-src[i,0])**2+(tempDst[j,1] -
                                                     src[i,1])**2+(tempDst[j,2]-src[i,2])**2
                if (dist < minDist):
                    minDist = dist
                    nearestIdx = j
            nearestNbrs.append(tempDst[nearestIdx])
            np.delete(tempDst,nearestIdx,0)
        return nearestNbrs


    def findRot(self, src, dst):
        # tempsrc = np.asarray(src.copy())
        # tempdst = np.asarray(dst.copy())
        centroid_A = np.mean(src, axis=0)
        centroid_B = np.mean(dst, axis=0)
        AA = src - centroid_A
        BB = dst - centroid_B
        H = np.dot(AA.T, BB)
        U, S, Vt = np.linalg.svd(H)
        return np.dot(Vt.T, U.T)

if __name__ == "__main__":
    src = []
    dst = []
    aligner = icp()
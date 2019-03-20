#!/usr/bin/python

import cv2 as cv


class genVideo:
    def __init__(self):
        img = []
        for i in range(0,46):
            img.append(cv.imread('/home/zhangtianyi/data/2018_04_17_222408/'+str(i)+'.png'))
            print(i)

        height,width,layers=img[0].shape
        fourcc = cv.VideoWriter_fourcc(*'H264')
        # video=cv.VideoWriter('video.avi',-1,1,(width,height))
        video=cv.VideoWriter('output.MP4',fourcc, 5.0, (width/2,height/2),1)

        for j in range(0,46):
            video.write(img[j])

        cv.destroyAllWindows()
        video.release()

if __name__ == "__main__":
    vid = genVideo()

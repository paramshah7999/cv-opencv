import cv2 as cv
import os 
import matplotlib.pyplot as plt
import numpy as np 

#check cv installation and version
#if __name__ == '__main__':
    #print(cv.__version__)

def readImage():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoImages\\cutepic1.jpg')

    #matrix (M, N, 3)
    img = cv.imread(imgPath)

    #pass in (name of image, matrix)
    cv.imshow('img', img)
    cv.waitKey(0)




if __name__ == "__main__":
    readImage
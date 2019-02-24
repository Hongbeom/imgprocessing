import cv2
import numpy as np
import random

original  = cv2.imread("test.png", 1)
#gray  = cv2.imread("test.jpg", 0)
#unchange = cv2.imread("test.jpg", -1)

x = original.shape[1]
y = original.shape[0]

print(x, y)

tmp = original.copy()

def Rotate(src, degree):
	if degree is 90:
		dst = cv2.transpose(src)
		dst = cv2.flip(dst, 1)
	elif degree is 180:
		dst = cv2.flip(src, -1)
	elif degree is 270:
		dst = cv2.transpose(src)
		dst = cv2.flip(dst, 0)
	return dst


def randomRotate(key, img):
	height, width, channel = img.shape
	dst = None
	if(key is 0): 
		dst = cv2.flip(img, 0)
	elif(key is 1):
		dst = cv2.flip(img, 1)
	elif(key is 2):
		dst = Rotate(img, 90)
	elif(key is 3):
		dst = Rotate(img, 180)
	elif(key is 4):
		dst = Rotate(img, 270)

	return dst

imgList = []



first = tmp[0:int(y/2), 0:int(x/2)]
second = tmp[0:int(y/2), int(x/2):x]
third = tmp[int(y/2):y, 0:int(x/2)]
fourth = tmp[int(y/2):y, int(x/2):x]



imgList.append(first)
imgList.append(second)
imgList.append(third)
imgList.append(fourth)

for i in range(len(imgList)):
	cv2.imwrite("enced/" + str(i) + '.png', randomRotate(random.randrange(0,5), imgList[i]))





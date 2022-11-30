from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("azad.jpeg")
image= cv2.resize(image, (1080,900))
# cv2.waitkey(0)
s = image.shape
cv2.imshow('original',image)

# print(s)
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageGray = cv2.convertScaleAbs(imageGray, alpha=1.10, beta=-20)
cv2.imshow('Binary', imageGray)
def Hist(image):
    H = np.zeros(shape=(256,1))
    s = image.shape
    for i in range(s[0]):
      for j in range(s[1]):
          k=imageGray[i,j]
          H[k,0]=H[k,0]+1
    return H
histg = Hist(imageGray)
plt.plot(histg)
x = histg.reshape(1,256)
y = np.array([])
y = np.append(y,x[0,0])
for i in range(255):
    k= x[0,i+1] + y[i]
    y = np.append(y,k)
y = np.round((y/(s[0]*s[1]))*(256-1))
for i in range(s[0]):
    for j in range(s[1]):
        k = imageGray[i,j]
        imageGray[i,j]= y[k]
equal = Hist(imageGray)
cv2.imshow("myequalize",imageGray)
plt.plot(equal)
plt.show()
cv2.waitkey(0)



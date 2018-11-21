import cv2
import os

a = os.listdir('.\\1\\')
for i in range(len(a)):
    path = '.\\1\\' + a[i]
    img = cv2.imread(path)
    path = '.\\1\\' + str(i) + '.jpg'
    cv2.imwrite(path, img)
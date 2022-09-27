import cv2
import os
os.mkdir("Frames")
os.mkdir("ROI")


count=0
Video=cv2.VideoCapture('video.mp4')
length = int(Video. get(cv2. CAP_PROP_FRAME_COUNT))
length = int(Video. get(cv2. CAP_PROP_FRAME_COUNT))
print(length)
while Video.isOpened():
    count=count + 1
    sema,frame = Video.read()
    if sema == True:
        cv2.imwrite('Frames/Frame'+str(count)+".jpg",frame)
        print(''+str(count))


li=[]
num=int(length/2)
print(num)
for i in range(1,num):
    li.append('Frame'+str(i)+".jpg")
print(li)


for i in range(0,len(li)):
    img=cv2.imread("Frames/"+li[i])
    face = img[150:600, 350:630]
    cv2.imwrite('ROI/'+li[i], face)


li01=[]
import numpy as np
for i in range(0,len(li)):
    img=cv2.imread('ROI/'+li[i])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    try:
        for rho, theta in lines[0]:
            try:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))

                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            except:
                pass
        try:
            li01.append(li[i])
        except:
            pass
    except:
        print('Nothing found')

print(li01)


import shutil
shutil.rmtree("ROI")
shutil.rmtree("Frames")

import cv2
import numpy as np

img = cv2.imread('/Users/vamshibukya/Desktop/pythonProject/frame001.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
try:
    for rho,theta in lines[0]:
        try:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        except:
            pass
    try:
        cv2.imwrite('houghlines3.jpg',img)
    except:
        pass
except:
    print('Nothing found')
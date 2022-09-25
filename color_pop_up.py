import cv2



image=cv2.imread('/Users/vamshibukya/Desktop/pythonProject/Datasets/Train/Appium/frame_247.jpg')
hsv_nemo = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
lower = (50, 100, 100)
upper = (70, 255, 255)
mask = cv2.inRange(hsv_nemo, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)



cv2.imwrite('frame001.jpg',result)
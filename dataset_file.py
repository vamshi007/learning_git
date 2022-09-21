import cv2

cap=cv2.VideoCapture('/Users/vamshibukya/Desktop/pythonProject/video.mp4')
count=0
while cap.isOpened():
    count += 1
    ret, frame = cap.read()
    if ret == True:
        start_point_01 = (640 , 0 )
        end_point_01 = (640,720)
        start_point_02=(0,640)
        end_point_02=(1280,640)
        color = (0, 255, 0)
        thickness = 1
        image = cv2.line(frame, start_point_01, end_point_01, color, thickness)
        image = cv2.line(image, start_point_02, end_point_02, color, thickness)
        cv2.imwrite("frame_"+str(count)+'.jpg', image)
    else:
        break


        
cap=cv2.VideoCapture('/Users/vamshibukya/Desktop/pythonProject/video.mp4')
count=0
while cap.isOpened():
    count += 1
    ret, frame = cap.read()
    if ret == True:
        cv2.imwrite("frame_"+str(count)+'.jpg', frame)
    else:
        break

import cv2
import datetime
import time
cap = cv2.VideoCapture('test_01_video.mp4')
count = 0

while (cap.isOpened()):
    count += 1
    # print(count)
    ret, frame = cap.read()
    if ret == True:
        if count==80:
            start_time = datetime.datetime.now()
        if count ==121:
            end_time = datetime.datetime.now()
        if count > 80 and count <121:
            cv2.imshow('Frame', frame)
            # cv2.putText(frame, "{}: {:.2f}".format(text, fm), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    else:
        break
print(end_time-start_time)
print(start_time)
print(end_time)

cap.release()
cv2.destroyAllWindows()
print(count)

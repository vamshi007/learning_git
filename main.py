import cv2
import time
cap = cv2.VideoCapture('test_01_video.mp4')
count = 0


def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()


while (cap.isOpened()):
    time.sleep(1)
    count += 1
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        if fm > 100:
            text = "Stable"+str(count)
        else:
            text = "Un_stable"+str(count)
        cv2.putText(frame, "{}: {:.2f}".format(text, fm), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
print(count)

https://drive.google.com/file/d/1tL2m923OhjPjc1pb-4YfvBIXi7RyBuAM/view?usp=drivesdk

import cv2
import easyocr
import math
import os

filename = os.listdir()
li_filename = []
reader = easyocr.Reader(['ch_sim','en'],gpu=False)
for file in filename:
    if file.endswith('.jpeg'):
        li_filename.append(file)
li_filename=sorted(li_filename)
ki=[]
for i in range(len(li_filename)):
    image=cv2.imread(li_filename[i])
    x=image.shape[0]
    y = image.shape[1]
    cropped_img = image[math.ceil(y*0.12):math.ceil(y*0.80), math.ceil(x*0.02):math.ceil(x*0.85)]
    result = reader.readtext(cropped_img,detail=0)
    k=""
    result=str(result)
    for j in range(len(result)):
        try:
            if type(int(result[j]))==int:
                k=k+result[j]
        except:
            pass
    ki.append(k)
ki=sorted(ki,reverse=True)
print(ki)
for i in range(len(ki)):
    if i==len(ki)-1:
        break
    else:
        print(int(ki[i])-int(ki[i+1]))









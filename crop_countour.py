import cv2

image= cv2.imread('/content/image.jpg')
original_image= image

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges= cv2.Canny(gray, 50,200)


contours, hierarchy= cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)



for (i,c) in enumerate(sorted_contours):
    x,y,w,h= cv2.boundingRect(c)
    
    cropped_contour= original_image[y:y+h, x:x+w]
    image_name= "output_shape_number_" + str(i+1) + ".jpg"
    cv2.imwrite(image_name, cropped_contour)
    readimage= cv2.imread(image_name)
    cv2.imwrite('Image.jpg', readimage)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()

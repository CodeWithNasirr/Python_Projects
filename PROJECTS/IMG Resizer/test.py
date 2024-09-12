import cv2

old_img="IMG.jpg"
new_img="New.jpg"
new_size=(600,400)

img=cv2.imread("3.jpg")
resize_img=cv2.resize(img,new_size,cv2.INTER_AREA)

cv2.imwrite(new_img,resize_img)
print('Reize Img Sucessfully..')
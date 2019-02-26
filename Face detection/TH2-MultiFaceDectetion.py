from mtcnn.mtcnn import MTCNN
import os
import cv2

detector = MTCNN()

img = cv2.imread("image\img02.jpg")
img_temp = img.copy()
img_crop = []
result = detector.detect_faces(img)

count = 1
for faces in result:
    bounding_box = faces['box']

    cv2.rectangle(
        img_temp,
        (bounding_box[0],bounding_box[1]),
        (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
        (220,20,60)
    )

    img_crop = img_crop.append(img[bounding_box[1]:bounding_box[1] + bounding_box[3],bounding_box[0]:bounding_box[0] + bounding_box[2]])
    cv2.imwrite(os.path.join('image_crop', str(count) + ".jpg"),img_crop)
    count = count + 1

cv2.imshow("Multi faces detection", img_temp)

cv2.waitKey()
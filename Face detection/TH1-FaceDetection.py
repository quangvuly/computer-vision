from mtcnn.mtcnn import MTCNN
import cv2

detector = MTCNN()

img = cv2.imread("image\img01.jpg")
result = detector.detect_faces(img)

bounding_box = result[0]['box']
cv2.rectangle(
    img,
    (bounding_box[0],bounding_box[1]),
    (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
    (220,20,60),
    2
)

cv2.imshow('Face detection',img)

cv2.waitKey()
from mtcnn.mtcnn import MTCNN 
from urllib.request import urlopen

import numpy as np 
import urllib
import matplotlib.pyplot as plt 
import cv2

url = 'http://www.catholicteacher.com/wp-content/uploads/2014/01/business-people-talking.jpg'
def url2image(url):
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()),dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


img_process = url2image(url)

detector = MTCNN()
result = detector.detect_faces(img_process)
print(result)



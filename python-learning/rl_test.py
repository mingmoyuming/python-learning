# -*- coding: utf-8 -*-
import numpy
import cv2
import sys
from PIL import Image,ImageDraw
import MySQLdb

# imagepath = r'E:\hey6.jpg'
# # # db = MySQLdb.connect()
# #
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
# #face_cascade.load('E:\a small program every day\haarcascade_frontalface_alt2.xml')
# image = cv2.imread(imagepath)
#
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#
# faces = face_cascade.detectMultiScale(
#     gray,
#     scaleFactor=1.3,
#     minNeighbors=5,
#     minSize=(5,5),
# #    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
# )
#
# print("发现{0}张".format(len(faces)))
#
# for(x,y,w,h) in faces:
#     image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
# try:
#     image_test = cv2.resize(image,(int(x / 2),int(y / 1)))
# except NameError as e:
#     print("图片中都是些丑逼，识别不出来")
# cv2.imshow("find Faces!",image_test)
# cv2.waitKey(0)

# 视频：
imagepath = r'E:\002.mp4'
# # db = MySQLdb.connect()
#

def catchvideo(window_name,camera_idx):
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(camera_idx)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#face_cascade.load('E:\a small program every day\haarcascade_frontalface_alt2.xml')
#image = cv2.imread(imagepath)
    while cap.isOpened():
        ok,frame = cap.read()
        if not ok:
            break

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        count = 0
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(5, 5),
            #    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        if len(faces) > 0:
            count = count + 1
    return count

if __name__ ==  '__main__':
    result = catchvideo("识别人脸",imagepath)
    if result > 0:
        print("此视频有%s个人" %result)
    else:
        print("没人")

# print("发现{0}张".format(len(faces)))
#
# for(x,y,w,h) in faces:
#     image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
# try:
#     image_test = cv2.resize(image,(int(x / 2),int(y / 1)))
# except NameError as e:
#     print("图片中都是些丑逼，识别不出来")
# cv2.imshow("find Faces!",image_test)
# cv2.waitKey(0)
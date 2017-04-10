# coding: UTF-8
'''''''''''''''''''''''''''''''''''''''''''''''''''''
   file name: testModel.py
   create time: 2017年03月31日 星期五 15时48分05秒
   author: Jipeng Huang
   e-mail: huangjipengnju@gmail.com
   github: https://github.com/hjptriplebee
'''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import alexnet
import cv2
import tensorflow as tf
import numpy as np
import caffe_classes

#some params
dropoutPro = 1
classNum = 1000
skip = []
#get testImage
testPath = "testModel"
testImg = []
for f in os.listdir(testPath):
    testImg.append(cv2.imread(testPath + "/" + f))

imgMean = np.array([104, 117, 124], np.float)
x = tf.placeholder("float", [1, 227, 227, 3])

model = alexnet.alexNet(x, dropoutPro, classNum, skip)
score = model.fc3
softmax = tf.nn.softmax(score)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    model.loadModel(sess)

    for i, img in enumerate(testImg):
        #img preprocess
        test = cv2.resize(img.astype(np.float), (227, 227))
        test -= imgMean
        test = test.reshape((1, 227, 227, 3))
        maxx = np.argmax(sess.run(softmax, feed_dict = {x: test}))
        res = caffe_classes.class_names[maxx]
        #print(res)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, res, (int(img.shape[0]/3), int(img.shape[1]/3)), font, 1, (0, 255, 0), 2)
        cv2.imshow("demo", img)
        cv2.waitKey(5000)

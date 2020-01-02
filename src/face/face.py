# -*- coding:utf-8 -*-
import cv2
import sys
import os
import shutil

args = sys.argv
argc = len(args)

if(argc != 2):
	print('引数を指定して実行してください。')
	quit()

image_path = args[1]

cascade_path = "./data/haarcascades/haarcascade_frontalface_alt.xml"

#ファイル読み込み
print(image_path)
image = cv2.imread(image_path)
if(image is None):
	print('画像を開けません。')
	quit()

#グレースケール変換
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)

#物体認識（顔認識）の実行
facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))

print("face rectangle")
print(facerect)
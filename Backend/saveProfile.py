import cv2
import dlib
import face_recognition
import numpy as np
import json

vid = cv2.VideoCapture(0) 
enc = None


def add(name,path):
	global js
	base_image = cv2.imread(path)
	sd = face_recognition.face_encodings(base_image)

	enc = {}
	enc["name"]=name
	enc["Encoding"]=sd[0].tolist()

	js["encodes"].append(enc)

js = {}
js["encodes"]=[]

add("Yash","../Faces/detectedYash.jpg")
add("Obama","../Faces/obama.jfif")
add("Trump","../Faces/trump.webp")
add("Modi","../Faces/modi.jpg")

# print(js)
with open('data.json', 'w') as outfile:
    json.dump(js, outfile)
from tkinter import *
from tkinter import filedialog
import os
import cv2 as cv
import numpy as np

root = Tk()

def rescaleFrame(frame, scale = 0.75): #rescala tanto los videos como las imagenes a un 75% porque me llenaba la pantalla entera
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def browseFiles():
    file = filedialog.askopenfilename(initialdir = "", title = "Select a File", filetypes = (("all files", "*.*"), ("Text files", "*.txt*"))) #Pide el archivo

    if file.lower().endswith(('.mp4')): #Abre solo los videos
      capture = cv.VideoCapture(file)

      while True:
        istrue, frame = capture.read()

        if type(frame) is type(None): #para que no salte el error -250
            break
        haar_cascade = cv.CascadeClassifier('haar_face.xml')
        faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 10)
        for (x, y, w, h) in faces_rect: #Comentar si no quieres que salga el recuadro al rededor de la cara
          cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)
          cv.imshow('https://github.com/Juan-Embid/Blurfaces', rescaleFrame(frame))
      
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    if file.lower().endswith(('.jpg', '.png')): #Abre solo las imagenes
      img = cv.imread(file)
      haar_cascade = cv.CascadeClassifier('haar_face.xml')
      faces_rect = haar_cascade.detectMultiScale(img, scaleFactor = 1.1, minNeighbors = 10)

      for (x, y, w, h) in faces_rect: #Comentar si no quieres que salga el recuadro al rededor de la cara
          cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)
          average = cv.blur(img, (10,10)) #Difumina la cara
          cv.imshow('https://github.com/Juan-Embid/Blurfaces', rescaleFrame(average))


def openCamera():
  os.system('cmd /c "start microsoft.windows.camera:"')

browse = Button(root, text = "Browse files", command = browseFiles)
browse.pack()
camera = Button(root, text = "Open camera", command = openCamera)
camera.pack()
root.title("BlurApp")
root.geometry("600x300")
root.mainloop()
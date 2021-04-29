from tkinter import *
from tkinter import filedialog
import os
import cv2
from tkinter.filedialog import asksaveasfile

root = Tk()

def rescaleFrame(frame, scale = 0.75): #rescala tanto los videos como las imagenes a un 75% porque me llenaba la pantalla entera
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

def browseFiles():
    file = filedialog.askopenfilename(initialdir = "", title = "Select a File", filetypes = (("all files", "*.*"), ("Text files", "*.txt*"))) #Pide el archivo

    if file.lower().endswith(('.mp4')): #Abre solo los videos
      cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
      capture = cv2.VideoCapture(file)

      def find_blur(bw, color):
        faces = cascade.detectMultiScale(bw, 1.1, 7)

        for (x, y, w, h) in faces:
          #cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)
          blur = color[y:y+h, x:x+w] #selecciona las caras
          gauss = cv2.GaussianBlur(blur, (101,101), 0) #Difumina la cara
          color[y:y+h, x:x+w] = gauss #vuelve a pegar la cara en la imagen

        return color

      while True:
        _, color = capture.read()
        if type(color) is type(None): #para que no salte el error -250
          break
        bw = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        cara = find_blur(bw, color)
        cv2.imshow('https://github.com/Juan-Embid/Blurfaces', rescaleFrame(cara))
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

    if file.lower().endswith(('.jpg', '.png', 'jfif')): #Abre solo las imagenes
      cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

      def find_blur(bw, color):
        faces = cascade.detectMultiScale(bw, 1.1, 7)

        for (x, y, w, h) in faces:
          #cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)
          blur = img[y:y+h, x:x+w] #selecciona las caras
          gauss = cv2.GaussianBlur(blur, (101,101), 0) #Difumina la cara
          img[y:y+h, x:x+w] = gauss #vuelve a pegar la cara en la imagen
        return color
      img = cv2.imread(file)
      bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      cara = find_blur(bw, img)
      cv2.imshow('https://github.com/Juan-Embid/Blurfaces', rescaleFrame(cara))

def openCamera():
  os.system('cmd /c "start microsoft.windows.camera:"')

browse = Button(root, text = "Browse files", command = browseFiles)
browse.pack()
camera = Button(root, text = "Open camera", command = openCamera)
camera.pack()
root.title("BlurApp")
root.geometry("600x300")
root.mainloop()
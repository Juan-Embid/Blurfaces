import cv2
import numpy as np
import dlib
import math
from quickHull import *

detector = dlib.get_frontal_face_detector() #Carga el detector
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Carga el predictor para ver la forma
img = cv2.imread("download (2).jfif") #Lee imagen
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) #Lo pasa a escala de grises (mejor a la hora de detectar caras)
faces = detector(gray)

def rescaleFrame(frame, scale = 0.50): #rescala tanto los videos como las imagenes
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

def calculo_distancia(x1, y1, x2, y2): #El modulo
    dist = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

    return dist

def despeje_ptoMedio(x1, y1, x2, y2): #Con la ecuacion del punto medio
    Mx = (x2 * 2) - x1
    My = (y2 * 2) - y1

    return Mx, My

def puntos_circunferencia(P1, P2, Cx, Cy): #Puntos polares, basicamente saca una coordenada de una circunferencia
    P1x = P1 - Cx
    dist = calculo_distancia(P1, P2, Cx, Cy)
    deg = math.acos(P1x / dist)
    C1x = Cx + dist * math.cos((0.785398163397 / 2) + deg)
    C1y = Cy - dist * math.sin((0.785398163397 / 2) + deg)
    C2x = Cx + dist * math.cos(deg -(0.785398163397 / 2))
    C2y = Cy - dist * math.sin(deg -(0.785398163397 / 2))

    return C1x, C1y, C2x, C2y

def find_blur(gray, img, MPx, MPy, Ok1X, Ok1Y, Ok2X, Ok2Y, x, y): #comentar esta funcion, no funciona
 
        blur = img[y:y, x:x] #selecciona las caras
        gauss = cv2.GaussianBlur(blur, (101,101), 0) #Difumina la cara
        img[y:y+h, x:x+w] = gauss #vuelve a pegar la cara en la imagen

        blur = img[y:MPy, x:MPx]
        gauss = cv2.GaussianBlur(blur, (101,101), 0)
        img[y:MPy, x:MPx] = gauss

        blur = img[y:Ok1Y, x:Ok1X]
        gauss = cv2.GaussianBlur(blur, (101,101), 0)
        img[y:MPy, x:MPx] = gauss

        blur = img[y:Ok2Y, x:Ok2X]
        gauss = cv2.GaussianBlur(blur, (101,101), 0)
        img[y:MPy, x:MPx] = gauss

        return color

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    landmarks = predictor(image=gray, box=face)

    for n in range(0, 34): #Obtiene los puntos de la cara
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        Mx, My = despeje_ptoMedio(landmarks.part(33).x, landmarks.part(33).y, landmarks.part(28).x, landmarks.part(28).y)
        MPx, MPy = despeje_ptoMedio(landmarks.part(28).x, landmarks.part(28).y, Mx, My)
        Ok1X, Ok1Y, Ok2X, Ok2Y = puntos_circunferencia(MPx, MPy, landmarks.part(33).x, landmarks.part(33).y)
        cv2.circle(img=img, center=(round(MPx), round(MPy)), radius=3, color=(255, 0, 0), thickness=-1)
        cv2.circle(img=img, center=(round(Ok1X), round(Ok1Y)), radius=3, color=(255, 0, 0), thickness=-1)
        cv2.circle(img=img, center=(round(Ok2X), round(Ok2Y)), radius=3, color=(255, 0, 0), thickness=-1)
        cv2.circle(img=img, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1) #Dibuja los puntos, comentar
        cv2.circle(img=img, center=(landmarks.part(33).x, landmarks.part(33).y), radius=3, color=(0, 0, 255), thickness=-1) #Centro de la circunferencia
        quickHull([[MPx, MPy], [Ok1X, Ok1Y], [Ok2X, Ok2Y], [landmarks.part(n).x, landmarks.part(n).y]]);
        #print(hull) #imprime el resultado de hacer el quickhull de todos los puntos de cada cara
        #cara = find_blur(gray, img, MPx, MPy, Ok1X, Ok1Y, Ok2X, Ok2Y, x, y) #Descomentar esta funcion
cv2.imshow(winname="https://github.com/Juan-Embid", mat=rescaleFrame(cara)) #Un poco de spam por aqui xd
cv2.waitKey(delay=0)
cv2.destroyAllWindows()
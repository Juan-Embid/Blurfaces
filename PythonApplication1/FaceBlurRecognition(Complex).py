import cv2
import numpy as np
import dlib
import cmath

detector = dlib.get_frontal_face_detector() #Carga el detector
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Carga el predictor para ver la forma
img = cv2.imread("download (2).jfif") #Lee imagen
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) #Lo pasa a escala de grises (mejor a la hora de detectar caras)
faces = detector(gray)
def calculo_puntosExtra(x1, y1, x2, y2):
    dist = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    landmarks = predictor(image=gray, box=face)
    for n in range(0, 34): #Obtiene los puntos de la cara
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        if (n == 28):
          ok28 = True
        elif (n == 34):
          ok34 = True
        if ((ok28 == True) and (ok34 == True)):
            calculo_puntosExtra(landmarks.part(28).x, landmarks.part(28).x, landmarks.part(34).x, landmarks.part(34).x)
        cv2.circle(img=img, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1) #Dibuja los puntos, comentar
cv2.imshow(winname="https://github.com/Juan-Embid", mat=img) #Un poco de spam por aquí xd
cv2.waitKey(delay=0)
cv2.destroyAllWindows()
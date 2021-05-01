import cv2
import numpy as np
import dlib
import math

detector = dlib.get_frontal_face_detector() #Carga el detector
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Carga el predictor para ver la forma
img = cv2.imread("download (2).jfif") #Lee imagen
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) #Lo pasa a escala de grises (mejor a la hora de detectar caras)
faces = detector(gray)
def calculo_distancia(x1, y1, x2, y2):
    dist = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return dist
def calculo_ptoMedio(x1, y1, x2, y2):
    M1 = (x1 + y1) / 2
    M2 = (x2 + y2) / 2
    return M1, M2
def despeje_ptoMedio(x1, y1, x2, y2):
    Mx = (x2 * 2) - x1
    My = (y2 * 2) - y1
    return Mx, My
def puntos_circunferencia(P1, P2, Cx, Cy):
    P1x = P1 - Cx
    dist = calculo_distancia(P1, P2, Cx, Cy)
    deg = math.acos(P1x / dist)
    C1x = Cx + dist * math.cos(0.785398163397 + deg)
    C1y = Cy - dist * math.sin(0.785398163397 + deg)
    C2x = Cx + dist * math.cos(deg -0.785398163397)
    C2y = Cy - dist * math.sin(deg -0.785398163397)
    return C1x, C1y, C2x, C2y
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    landmarks = predictor(image=gray, box=face)
    for n in range(0, 34): #Obtiene los puntos de la cara
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        if (n < 28):
          ok28 = False
        elif (n == 28):
          ok28 = True
        if (n < 33):
          ok33 = False
        elif (n == 33):
          ok33 = True
        if ((ok28 == True) and (ok33 == True)):
            Mx, My = despeje_ptoMedio(landmarks.part(33).x, landmarks.part(33).y, landmarks.part(28).x, landmarks.part(28).y)
            MPx, MPy = despeje_ptoMedio(landmarks.part(28).x, landmarks.part(28).y, Mx, My)
            #P1, P2 = calculo_ptoMedio(landmarks.part(28).x, landmarks.part(28).y, Mx, My)
            #distancia = calculo_distancia(P1, P2, Mx, My)
            #C1x, C1y, C2x, C2y = puntos_circunferencia(distancia, P1, P2)
            Ok1X, Ok1Y, Ok2X, Ok2Y = puntos_circunferencia(MPx, MPy, landmarks.part(33).x, landmarks.part(33).y)
            cv2.circle(img=img, center=(round(MPx), round(MPy)), radius=3, color=(255, 0, 0), thickness=-1)
            cv2.circle(img=img, center=(round(Ok1X), round(Ok1Y)), radius=3, color=(255, 0, 0), thickness=-1)
            cv2.circle(img=img, center=(round(Ok2X), round(Ok2Y)), radius=3, color=(255, 0, 0), thickness=-1)
            cv2.circle(img=img, center=(round(MPx), round(MPy)), radius=3, color=(255, 0, 0), thickness=-1)
        cv2.circle(img=img, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1) #Dibuja los puntos, comentar
        cv2.circle(img=img, center=(landmarks.part(33).x, landmarks.part(33).y), radius=3, color=(0, 0, 255), thickness=-1)
cv2.imshow(winname="https://github.com/Juan-Embid", mat=img) #Un poco de spam por aqu� xd
cv2.waitKey(delay=0)
cv2.destroyAllWindows()
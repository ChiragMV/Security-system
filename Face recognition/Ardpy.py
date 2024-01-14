import cv2
import pyfirmata
import time
port="COM8"
board = pyfirmata.Arduino(port)
face_classifier = cv2.CascadeClassifier('haarcascade_profileface.xml')
chirag_model = cv2.face.LBPHFaceRecognizer_create()
chirag_model.read('chirag.yml')
def face_detector(img,size=0.5):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is ():
        return img,[]
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h,x:x+w]
        roi = cv2.resize(roi,(200,200))
    return img,roi
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    image,face = face_detector(frame)
    try:
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        results = chirag_model.predict(face)
        if results[1]<500:
            confidence = int(100*(1-(results[1])/400))
            display_string = str(confidence)+'% Confident it is Chirag'
        if confidence<=1:
            cv2.putText(image,"Recognizing Face ...",(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(57,255,20),2)
            board.digital[6].write(0)
        if confidence>50:
            cv2.putText(image,"Opening Door:  Welcome Chirag",(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(57,255,20),2)
            cv2.imshow("Face recognition",image)
            board.digital[6].write(1)
            time.sleep(14)
            board.digital[6].write(0)
            break
        else:
            board.digital[6].write(0)
            cv2.putText(image,"I don't know, who are you?",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            cv2.imshow("Face Recognition",image)
    except:
        cv2.putText(image,"No Face found",(220,120),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.putText(image,"Looking for face",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow("Face Recognition",image)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
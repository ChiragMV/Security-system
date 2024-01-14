import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
import os

#Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Load functions
def face_extractor(img):
    #Function detects faces&returns cropped face. If no face detected, it return input image
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if len(faces)==0:
        return None
    #Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h ,x:x+w]
    return cropped_face
#initialize webcam
cap=cv2.VideoCapture(0)
count=0
#Collect 100 samples of face from webcam input
while True:
    ret,frame=cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        #Save file in specified directory with unique name
        file_name_path = './faces/'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)
        #Put count on images and display live count
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Cropper',face)
    else:
        print("Face not found")
        pass
    if cv2.waitKey(1)==13 or count==100:#13 is the Enter key
        break
cap.release()
cv2.destroyAllWindows()
print("Colecting samples complete")

data_path='./faces/'
os.makedirs(data_path, exist_ok=True)
onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]
Training_Data,Labels=[],[]
for i,files in enumerate(onlyfiles):
    image_path=data_path+onlyfiles[i]
    images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images,dtype=np.uint8))
    Labels.append(i)
Labels = np.asarray(Labels,dtype=np.int32)
chirag_model=cv2.face.LBPHFaceRecognizer_create()
chirag_model.train(np.asarray(Training_Data),np.asarray(Labels))
print("Model trained successfully")
chirag_model.write('chirag.yml')
chirag_model=cv2.face.LBPHFaceRecognizer_create()
chirag_model.read('chirag.yml')
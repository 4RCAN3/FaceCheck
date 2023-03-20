import cv2
import face_recognition
import os
import json, codecs

class Dataset():
    def __init__(self, images : list = None, id : str = None, known_faces : list = [], known_names : list = []) -> None:
        self.images = images
        self.id = id
        self.facesloc_ = []
        self.knownFaces_ = known_faces
        self.knownNames_ = known_names
        self.imageNum_ = len(images) if images != None else 0

    
    def AddFaceLocations(self) -> list:
        faces = self.facesloc_
        for image in self.images:
            face_locations = face_recognition.face_locations(image)
            for top, right, bottom, left in face_locations:
                face_image = image[top:bottom, left:right]
                faces.append(face_image)
        
        return faces
    
    def AddFaceEncodings(self, faces: list) -> None:
        face_encs = []
        c = 0
        for face in faces:
            face_encoding = face_recognition.face_encodings(face)
            if face_encoding != []:
                face_encs.append(face_encoding[0].tolist())
                c += 1

        self.knownFaces_.extend(face_encs)
        self.knownNames_.extend([self.id for i in range(c)])
    
    def WriteFaces(self) -> None:
        print(self.knownFaces_)
        toWrite = {"known faces" : list(self.knownFaces_), "known names" : list(self.knownNames_)}
        json.dump(toWrite, open('faces.json', 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)

class FacialDetection(Dataset):
    def __init__(self, images: list = None, id: str = None, known_faces: list = [], known_names: list = []) -> None:
        super().__init__(images, id, known_faces, known_names)

    def detect(self, frame) -> str:
        known_faces, known_names = self.knownFaces_, self.knownNames_
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for any of the known faces
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            # If there is a match, label the face with the name
            name = "Unknown"
            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]

            
            return name

class ImageList():

    def __init__(self) -> None:
        self.images = dict()

    def ProcessImage(self, uid, filename) -> None:
        img = cv2.imread(filename)
        if uid not in self.images.keys():
            self.images[uid] = [img]
        else:
            self.images[uid].append(img)


def Register(uid: str, imagePaths: list) -> None:
    imageData = ImageList()
    for path in imagePaths:
        imageData.ProcessImage(uid, path)
    
    images = imageData.images

    faces = json.loads(open('faces.json').read())
    for id in images:
        if id in faces['known names']:
            print('Id already registered')
            continue
        dataset = Dataset(images = images[id], id = id, known_faces=faces['known faces'], known_names=faces['known names'])
        faceLocs = dataset.AddFaceLocations()
        dataset.AddFaceEncodings(faceLocs)
        dataset.WriteFaces()

def Detect(filename: str) -> str:
    img = cv2.imread(filename)
    faces = json.loads(open('faces.json').read())
    detection = FacialDetection(known_faces = faces['known faces'], known_names = faces['known names'])
    name = detection.detect(img)
    
    return name

'''if __name__ == '__main__':
    imageData = ImageList()
    for imgFolder in os.listdir('data/'):
        for filename in os.listdir('data/' + imgFolder):
            filename = 'data/' + imgFolder + '/' + filename
            imageData.ProcessImage(imgFolder, filename)

    images = imageData.images

    faces = json.loads(open('faces.json').read())
    for id in images:
        if id in faces['known names']:
            continue
        dataset = Dataset(images = images[id], id = id, known_faces=faces['known faces'], known_names=faces['known names'])
        faceLocs = dataset.AddFaceLocations()
        dataset.AddFaceEncodings(faceLocs)
        dataset.WriteFaces()
    
    testImage = cv2.imread('test.jpeg')
    detection = FacialDetection(known_faces = faces['known faces'], known_names = faces['known names'])
    detection.detect(testImage)'''

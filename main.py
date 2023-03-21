import cv2
import face_recognition
import os
import json, codecs

class Dataset():
    def __init__(self, images : list = None, id : str = None, known_faces : list = [], known_names : list = []) -> None:
        """Create face encodings for a user to add to the set of known users

        Args:
            images (list, optional): A list of image objects that are processed to add face encodings. Defaults to None.
            id (str, optional): User id to which the list of images corresponds. Defaults to None.
            known_faces (list, optional): A list of known faces. Defaults to [].
            known_names (list, optional): A list of known names/uid that is mapped to the known faces. Defaults to [].
        """  

        self.images = images
        self.id = id
        self.facesloc_ = []
        self.knownFaces_ = known_faces
        self.knownNames_ = known_names
        self.imageNum_ = len(images) if images != None else 0

    
    def AddFaceLocations(self) -> list:
        """Marks the locations of face features

        Returns:
            faces (list): A numpy array of face features for each image
        """        
        faces = self.facesloc_
        for image in self.images:
            face_locations = face_recognition.face_locations(image)
            for top, right, bottom, left in face_locations:
                
                face_image = image[top:bottom, left:right]
                faces.append(face_image)
        
        return faces
    
    def AddFaceEncodings(self, faces: list) -> None:
        """Encode each face feature from the list of face features

        Args:
            faces (list): A list of face features that are marked
        """        

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
        """
        Write the json for known faces and their corresponding user ids to a file
        """        
        #print(self.knownFaces_)
        print(self.knownNames_)
        toWrite = {"known faces" : list(self.knownFaces_), "known names" : list(self.knownNames_)}
        json.dump(toWrite, open('./flask-server/FaceCheck/faces.json', 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)

class FacialDetection(Dataset):

    def __init__(self, images: list = None, id: str = None, known_faces: list = [], known_names: list = []) -> None:
        """
        Inherits the Dataset class and adds the 
        functionality of identifying one particular frame/image

        Args:
            images (list, optional): A list of image objects that are processed to add face encodings. Defaults to None.
            id (str, optional): User id to which the list of images corresponds. Defaults to None.
            known_faces (list, optional): A list of known faces. Defaults to [].
            known_names (list, optional): A list of known names/uid that is mapped to the known faces. Defaults to [].
        """        
        super().__init__(images, id, known_faces, known_names)

    def detect(self, frame) -> str:
        """
        A function to identify a frame and compare the known users

        Args:
            frame (obj): frame/imaje object to be detected

        Returns:
            name (str): User ID of the identified individual. Returns Unkown if not identified
        """    

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
        
        return name

class ImageList():

    def __init__(self) -> None:
        """
        A class to make a dictionary of user IDs
        with a list of their respective pictures 
        as values
        """        

        self.images = dict()

    def ProcessImage(self, uid, filename) -> None:
        """Processes a file to convert it an openCV img object

        Args:
            uid (str): User ID 
            filename (str): Path to the image that needs to be processed
        """        
        img = cv2.imread(filename)
        if uid not in self.images.keys():
            self.images[uid] = [img]
        else:
            self.images[uid].append(img)


def Register(uid: str, imagePaths: list) -> None:
    """
    A function to register a list of image paths that correspond to a user
    i.e register the user to known users

    Args:
        uid (str): User id
        imagePaths (list): A list of image paths that need to be added for processing 
    """    

    imageData = ImageList()
    for path in imagePaths:
        imageData.ProcessImage(uid, path)
    
    images = imageData.images

    faces = json.loads(open('./flask-server/FaceCheck/faces.json').read())
    for id in images:
        if id in faces['known names']:
            print('Id already registered')
            continue
        dataset = Dataset(images = images[id], id = id, known_faces=faces['known faces'], known_names=faces['known names'])
        faceLocs = dataset.AddFaceLocations()
        dataset.AddFaceEncodings(faceLocs)
        dataset.WriteFaces()

def Detect(filename: str) -> str:
    """
    A function to detect if a particular image belongs to a known user

    Args:
        filename (str): path to the file that needs to be identified

    Returns:
        name (str): the user id that is identified. Unknown if unidentified 
    """    
    img = cv2.imread(filename)
    faces = json.loads(open('./flask-server/FaceCheck/faces.json').read())
    detection = FacialDetection(known_faces = faces['known faces'], known_names = faces['known names'])
    name = detection.detect(img)
    
    return name
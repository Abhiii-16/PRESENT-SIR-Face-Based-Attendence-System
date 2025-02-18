import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time
from PIL import ImageTk, Image


def TrainImage(haarcasecade_path, message, text_to_speech):
    trainimage_path = os.path.join(os.getcwd(), "TrainingImage")
    trainimagelabel_path = os.path.join(os.getcwd(), "Trainner", "Trainner.yml")

    os.makedirs(trainimage_path, exist_ok=True)
    os.makedirs(os.path.dirname(trainimagelabel_path), exist_ok=True)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(haarcasecade_path)

    faces, Ids = getImagesAndLables(trainimage_path)
    recognizer.train(faces, np.array(Ids))
    recognizer.save(trainimagelabel_path)

    res = "Image Trained successfully"
    message.configure(text=res)
    text_to_speech(res)



def getImagesAndLables(path):
    # imagePath = [os.path.join(path, f) for d in os.listdir(path) for f in d]
    newdir = [os.path.join(path, d) for d in os.listdir(path)]
    imagePath = [
        os.path.join(newdir[i], f)
        for i in range(len(newdir))
        for f in os.listdir(newdir[i])
    ]
    faces = []
    Ids = []
    for imagePath in imagePath:
        pilImage = Image.open(imagePath).convert("L")
        imageNp = np.array(pilImage, "uint8")
        Id = int(os.path.split(imagePath)[-1].split("_")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids

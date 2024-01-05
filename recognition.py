import os
import cv2
from keras.models import load_model
import numpy as np
import pandas as pd
def recognition():
    detected_faces_folder = 'results/detected_faces_individual'
    image_files = os.listdir(detected_faces_folder)
    model = load_model('face_recognition_model_50.h5')
    attendance=set()
    for image_file in image_files:
        image_path = os.path.join(detected_faces_folder, image_file)
        image = cv2.imread(image_path)
        input_image = cv2.resize(image, (224, 224))  # Resize to match model input size
        input_image = np.expand_dims(input_image, axis=0)
        prediction = model.predict(input_image)
        max_index = np.argmax(prediction)
        attendance.add(max_index)
    print(attendance)
    df=pd.read_csv("dataset.csv")
    df
    df.drop("Timestamp",axis=1)
    email=df["Email Address"]
    roll_number=df["Roll Number"]
    name=df["Name"]
    data = {
        'Email Address':email,
        'Name': name,
        'Roll Number': roll_number
    }
    df1 = pd.DataFrame(data)
    def assign_attendance_status(index):
        if index in attendance:
            return 'Present'
        else:
            return 'Absent'
    df1['Attendance'] = df1.index.map(assign_attendance_status)
    df1.to_csv("attendance.csv", index=False) 



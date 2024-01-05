import cv2
from facenet_pytorch import MTCNN
import save
from PIL import Image
mtcnn = MTCNN(keep_all=True)
import os
def detect_faces():
    directory = 'results/raw_frames'
    image_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.jpg', '.png', '.jpeg'))]
    detected_faces=[]
    i=1
    for frame in image_paths:
        img = cv2.imread(frame)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Detect faces using MTCNN
        boxes, probs = mtcnn.detect(img_rgb)

        # Draw bounding boxes on the image
        if boxes is not None:
            for box in boxes:
                cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
        save_directory = 'results/detected_faces'
        os.makedirs(save_directory, exist_ok=True)
        saved_path = os.path.join(save_directory, f'frame_{i}.jpg')
        i+=1
        cv2.imwrite(saved_path,img)
        if boxes is not None:
            for i, box in enumerate(boxes):
                # Convert box coordinates to integers
                box = [int(coord) for coord in box]
                margin=15
                box[0] = max(0, box[0] - margin)  # x1
                box[1] = max(0, box[1] - margin)  # y1
                box[2] = min(img.shape[1], box[2] + margin)  # x2
                box[3] = min(img.shape[0], box[3] + margin)
                # Crop face region from the image
                face_roi = img[box[1]:box[3], box[0]:box[2]]
                detected_faces.append(face_roi)
                # Save the extracted face as a separate image
                

    return detected_faces

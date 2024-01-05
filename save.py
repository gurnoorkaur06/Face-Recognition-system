import cv2
import os
from shutil import rmtree
def save(images,folder):
    output_directory = f'results/{folder}'
    if os.path.exists(output_directory):
    # If folder exists, delete it and create a new one
        rmtree(output_directory)  # Delete the folder and its contents
        os.makedirs(output_directory)  # Recreate the folder
    else:
    # If folder doesn't exist, create it
        os.makedirs(output_directory, exist_ok=True)
    def save_frames(frames, output_dir):
        for i, frame in enumerate(frames, start=1):
            frame_filename = f"frame_{i}.jpg"
            frame_path = os.path.join(output_dir, frame_filename)
            cv2.imwrite(frame_path, frame)
    save_frames(images, output_directory)

import cv2
def frames(video_name):
    video_path = video_name
    cap = cv2.VideoCapture(video_path)
    images=[]
    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate the interval (in frames) to extract two frames per second
    interval = int(fps // 2)

    # Function to extract frames at a specific interval
    def extract_frames(video_capture):
        frame_count = 0

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if not ret:
                break

            frame_count += 1

            # Process the frame only if it's the desired frame according to the interval
            if frame_count % interval == 0:
                images.append(frame)

        video_capture.release()
    extract_frames(cap)
    return images

import os
def attendance(video):
    import recognition
    import frame
    import save
    import detect_faces
    import recognition
    video=os.path.join("download", video)
    images=frame.frames(video)
    save.save(images,"raw_frames")
    detected=detect_faces.detect_faces()
    save.save(detected,"detected_faces_individual")
    recognition.recognition()


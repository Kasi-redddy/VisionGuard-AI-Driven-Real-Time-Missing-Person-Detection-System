import cv2
import face_recognition
import numpy as np
import os
import datetime
import winsound  # For sound alerts in Windows
from flask import Flask, render_template, Response

app = Flask(__name__)

# Load known missing person images
missing_faces = []
missing_names = {}

missing_folder = "missing_persons"
if not os.path.exists(missing_folder):
    os.makedirs(missing_folder)

for file in os.listdir(missing_folder):
    img_path = os.path.join(missing_folder, file)
    image = face_recognition.load_image_file(img_path)
    encoding = face_recognition.face_encodings(image)
    if encoding:
        missing_faces.append(encoding[0])
        missing_names[tuple(encoding[0])] = os.path.splitext(file)[0]

video_capture = cv2.VideoCapture(0)  # Start live camera feed

# Ensure a directory for detected faces exists
if not os.path.exists("detected_faces"):
    os.makedirs("detected_faces")

def detect_faces():
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(missing_faces, face_encoding)
            name = "Unknown"
            color = (0, 255, 0)  # Green for unknown people

            if True in matches:
                match_index = matches.index(True)
                name = missing_names[tuple(missing_faces[match_index])]
                color = (0, 0, 255)  # Red for missing persons
                
                # Play alert sound
                winsound.Beep(1000, 500)

                # Save image as proof
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                cv2.imwrite(f"detected_faces/{name}_{timestamp}.jpg", frame)

            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect_faces(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

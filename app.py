import cv2
import numpy as np
import random
from flask import Flask, render_template, Response, jsonify, request

app = Flask(__name__)

# Load OpenCV's built-in, open-source Haar Cascade algorithms
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Global state tracker
current_challenge = "Blink Your Eyes"
challenge_verified = False
eyes_closed_detected = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_challenge')
def get_challenge():
    global current_challenge, challenge_verified, eyes_closed_detected
    # Simplified foolproof offline challenges using standard OpenCV tracking
    challenges = ["Blink Your Eyes", "Turn Face Left", "Turn Face Right"]
    current_challenge = random.choice(challenges)
    challenge_verified = False
    eyes_closed_detected = False
    return jsonify({"challenge": current_challenge})

@app.route('/verify_frame', methods=['POST'])
def verify_frame():
    global current_challenge, challenge_verified, eyes_closed_detected
    
    if challenge_verified:
        return jsonify({"status": "SUCCESS"})

    # Read the incoming image frame sent from the web front-end
    file = request.files['image'].read()
    np_img = np.frombuffer(file, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    
    # Convert to Grayscale for fast processing (< 1 second threshold constraint)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            
            # Detect eyes within the bounded face region
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            # 1. EVALUATE CHALLENGE: BLINK
            if current_challenge == "Blink Your Eyes":
                # If a face is visible but eyes drop to 0, user has closed their eyes
                if len(eyes) == 0:
                    eyes_closed_detected = True
                # Once eyes reappear after being closed, blink sequence is complete
                elif len(eyes) >= 1 and eyes_closed_detected:
                    challenge_verified = True
            
            # 2. EVALUATE CHALLENGE: TURN LEFT / RIGHT
            # When a face profile turns significantly, profile geometric aspect ratio changes
            elif current_challenge == "Turn Face Left":
                # In left turns, the eye detector loses symmetry or tracks single eye coordinates toward side
                if len(eyes) == 1 and (eyes[0][0] + eyes[0][2]/2) < w * 0.4:
                    challenge_verified = True
            
            elif current_challenge == "Turn Face Right":
                if len(eyes) == 1 and (eyes[0][0] + eyes[0][2]/2) > w * 0.6:
                    challenge_verified = True

    if challenge_verified:
        return jsonify({"status": "SUCCESS"})
    return jsonify({"status": "PENDING"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
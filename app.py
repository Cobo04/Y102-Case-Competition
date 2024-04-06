from flask import Flask, render_template, Response
from markupsafe import escape
from flask import url_for

import cv2
import qrcode
import numpy as np

# Flask and camera stream initializations

app = Flask(__name__)
camera = cv2.VideoCapture(0)
curS = "N/A"


# QR-Code Initializations
qcd = cv2.QRCodeDetector()


# Camera Stream

def generate_frames():
    global curS
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s:
                        # Print out the data
                        if s != curS:
                            curS = s
                            send_data(s)
                        color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)
                    cv2.polylines(frame, [p.astype(int)], True, color, 8)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame=buffer.tobytes()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def send_data(qr_data):
    print(qr_data)

# Flask setup and page mounts
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

# Backend
@app.route('/api/datapoint')
def api_datapoint():
    return curS


if __name__ == '__main__':
    app.run(debug=True)
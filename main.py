import qrcode
import numpy as np
import cv2

# Generate the QR Code with the correct data

data = "Test data about someone who is cool"
qr = qrcode.QRCode(version=1, box_size=10, border=4)

qr.add_data(data)
qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save("output.png")

# Open a webcam stream, outline the qrcode, and get the data

camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)
curS = ""

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    # Print out the data
                    if s != curS:
                        print(s)
                        curS = s
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)
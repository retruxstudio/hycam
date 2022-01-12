import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model 
import serial
import time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

msg = 0

mpface_detection = mp.solutions.face_detection
face_detection = mpface_detection.FaceDetection(min_detection_confidence=0.4)
mp_drawing = mp.solutions.drawing_utils

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Load gesture recognizer model
model = load_model('hycam.h5')

# Load class names
classNames = ['okay', 'peace', 'thumbs up', 'thumbs down', 'call me', 'stop', 'rock', 'live long', 'fist', 'smile']

root = Tk()

app_width = 1280
app_height = 720

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

root.title(' hycam - Please wait...')
root.iconbitmap('hycam.ico')
L1 = Label(root, bg="#ffffff")
L1.pack()

# Setup dan buka kamera
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)
# prevTime = 0

# Custom ukuran camera stream
cap.set(3,1280)
cap.set(4,720)

# Deklarasi serial monitor
ArduinoSerial=serial.Serial('com3', 115200, timeout=0.1)
time.sleep(1)

# Protokol saat menutup software hycam
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        keluar = "X0Y0C1"
        ArduinoSerial.write(keluar.encode('utf-8'))
        time.sleep(4)

def face():
    if results.detections:
        for id, detection in enumerate(results.detections):

            # Menampilkan anchor point face detection
            # mp_drawing.draw_detection(stream, detection)
            # print("ID: ", id, end='')

            # Simpan value koordinat wajah, contoh value:
            # xmin: 0.2537723481655121
            # ymin: 0.44607990980148315
            # width: 0.3164306581020355
            # height: 0.42188334465026855
            bBox = detection.location_data.relative_bounding_box
                
            # Simpan value ukuran camera stream, contoh value:
            # width: 640
            # height: 480
            # channel: 3
            # h, w, c = stream.shape

            # Kalkulasi koordinat dan ukuran wajah terhadap camera stream
            xb = int(bBox.xmin*w)
            yb = int(bBox.ymin*h)
            wb = int(bBox.width*w)
            hb = int(bBox.height*h)

            # Simpan value koordinat center wajah, contoh value: X313Y232
            koordinat='X{0:d}Y{1:d}C0'.format((xb+wb//2), (yb+hb//2))

            # Kirim value koordinat center wajah ke serial monitor
            ArduinoSerial.write(koordinat.encode('utf-8'))             

            # Menampilkan titik center dari wajah
            # cv2.circle(stream, (xb+wb//2, yb+hb//2), 2, (0,255,0), 2)

print ("""
  _                               
 | |                              
 | |__  _   _  ___ __ _ _ __ ___  
 | '_ \| | | |/ __/ _` | '_ ` _ \ 
 | | | | |_| | (_| (_| | | | | | |
 |_| |_|\__, |\___\__,_|_| |_| |_|
         __/ |                    
        |___/                     

A Smart camera for hybrid teaching.
Muhamad Rifaldi | 05311840000022

github.com/retruxstudio/hycam

""", end='')

while cap.isOpened():
    root.title(' hycam')
    stream = cap.read()[1]

    # Flip camera stream untuk set ke tampilan selfie
    stream = cv2.flip(stream, 1)

    # Set stream tidak writable untuk meningkatkan performance
    stream.flags.writeable = False
    
    # Convert stream color dari BGR menjadi RGB
    stream = cv2.cvtColor(stream, cv2.COLOR_BGR2RGB)    
    
    # Get hand landmark prediction
    result = hands.process(stream)

    # Memproses stream dan mendeteksi wajah
    results = face_detection.process(stream)

    className = ''
    
    # Set stream writable untuk visualisasi detection
    stream.flags.writeable = True

    # Convert kembali stream color menjadi BGR agar dapat ditampilkan
    stream = cv2.cvtColor(stream, cv2.COLOR_RGB2BGR)

    h, w, c = stream.shape

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * h)
                lmy = int(lm.y * w)
                landmarks.append([lmx, lmy])
            
            # Menampilkan hand landmarks
            mp_drawing.draw_landmarks(stream, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture, contoh value:
            # [[2.0691623e-18 1.9585415e-27 9.9990010e-01 9.7559416e-05 1.6617223e-06 1.0814080e-18 1.1070732e-27 4.4744065e-16 6.6466129e-07 4.9615162e-21]]
            prediction = model.predict([landmarks])
            
            classID = np.argmax(prediction)
            className = classNames[classID]

    if className == "stop":
        print("Camera go to mic location")
        kemic = "X0Y0C2"
        ArduinoSerial.write(kemic.encode('utf-8'))

    if className == "thumbs up":
        print("Camera back to default location")
        kedosen = "X0Y0C3"
        ArduinoSerial.write(kedosen.encode('utf-8'))    

    if className == "okay":
        msg += 1
        # print(msg)
        if msg == 2:
            print("Camera scaning onsite student")
            scansiswa = "X0Y0C4"
            ArduinoSerial.write(scansiswa.encode('utf-8'))
            msg = 0
            time.sleep(1)
    else:
        face()
    
    # Menampilkan save area detection
    # cv2.rectangle(stream, (1280//2-75,720//2-75), (1280//2+75,720//2+75), (255,255,255), 2)

    # Value FPS
    # currTime = time.time()
    # fps = 1 / (currTime - prevTime)
    # prevTime = currTime
    # print(f' | FPS: {int(fps)}', end='\r')

    # Menampilkan value FPS ke stream
    # cv2.putText(stream, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    stream = cv2.cvtColor(stream, cv2.COLOR_BGR2RGB)
    stream = ImageTk.PhotoImage(Image.fromarray(stream))
    L1['image'] = stream
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()

from gpiozero import MotionSensor
from picamera import PiCamera
import time
from datetime import datetime
from fractions import Fraction
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import config

print("BEGIN")

camera = PiCamera()
camera.resolution = (1920, 1080)
# camera.rotation = 180
print("Starting camera...")

out_path = "motion_captures/"

num = 0
pir = MotionSensor(4)
print("Waiting 30s while motion detector learns environment")

time.sleep(30)
while True:
    print("Starting motion detection...")
    pir.wait_for_motion()
    print("Motion detected!" + str(num))
    num += 1
    time.sleep(2)

    img_name = str(datetime.now())
    img_name = img_name.replace(" ", "-")
    img_name = img_name.replace(":", "-")
    img_name = img_name.replace(".", "-")

    img_name += ".jpg"

    camera.capture(out_path + img_name)
    print("Captured: {}".format(img_name))
    print("Sending image to recognize_faces_image.py...")
    CLICommand = 'python /home/pi/Development/edgar/face-recognition-opencv/recognize_faces_image2.py --encodings /home/pi/Development/edgar/face-recognition-opencv/encodings.pickle --image "/home/pi/Development/edgar/motion_captures/{imgName}" --detection-method hog'.format(
        imgName=img_name)
    f = os.popen(CLICommand)
    names = f.read()

    # Sending Email Notification
    sender_email = config.sender_email
    receiver_email = config.receiver_email
    password = config.password

    message = MIMEMultipart("alternative")
    message["Subject"] = "Person Detected"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = names
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("names returned: ")
    print(names)
    time.sleep(10)

print("END")

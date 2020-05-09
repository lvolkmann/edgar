from gpiozero import MotionSensor
from picamera import PiCamera
import time
from datetime import datetime
from fractions import Fraction

print("BEGIN")

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.rotation = 180
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
    num+= 1
    time.sleep(2)
    img_name = str(datetime.now()) + ".jpg"
    img_name = img_name.replace(" ", "-")
    camera.capture(out_path + img_name )
    print("Captured: {}".format(img_name))
    time.sleep(10)

print("END")

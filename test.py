from gpiozero import MotionSensor
from picamera import PiCamera
import time
from datetime import datetime
from fractions import Fraction

print("BEGIN")

'''
pir = MotionSensor(4)
num = 0
while True:
    pir.wait_for_motion()
    
    time.sleep(1)
    print("Motion detected!" + str(num))
    num += 1
'''

out_path = "captures/"

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.rotation = 180


print("Starting camera...")
time.sleep(1) # camera warm up


img_name = str(datetime.now()) + ".jpg"
camera.capture(out_path + img_name )

print("Captured: {}".format(img_name))

print("END")
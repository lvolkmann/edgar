EDGAR (or Eyeball the Door Grant Access upon Recognition) is a prototype IOT system meant to act as proof of concept for a face based home security locking system. The scope of this particular project is to detect motion, capture an image, run facial detection on that image, and then send an email to a specified account containing the system's prediction of who appears in that image.

# Hardware

* Raspberry Pi 3B+
* PiCamera
* Motion Sensor

# Setup

![](https://github.com/lvolkmann/edgar/blob/master/documentation/setup.jpg)

![](https://github.com/lvolkmann/edgar/blob/master/documentation/encoding.png)
> After physical system is set up, faces to be detected must be encoded and used to train the HAAR Cascades model. Around 20 images seemed to show acceptable results

# Results

![](https://github.com/lvolkmann/edgar/blob/master/documentation/detect_live.png)

![](https://github.com/lvolkmann/edgar/blob/master/documentation/email_results.png)

* Motion detection works reliably on a loop
* If no face is detected, an empty email is sent
* Prediction takes about 12 seconds
* Email is more or less instantaneous
* It takes 30 seconds for the motion sensor to “learn its environment”. Without initialization time, motion detector is far too sensitive
* Accuracy is incredibly reliable under normal conditions (low noise image with face directly at camera)
* Accuracy is slightly less reliable with low lighting and face at an angle of 45 degrees

# Future Work

* Integration with a smart lock system
* Integration with social media platforms to extend data set
* Add a user input feedback loop to further train the model
* Adding meta features like
  * Time of day
  * Day of year
  * Frequency of face detected
* Multi face detection
* Including confidence in notification
* Android/ios application for user settings, feedback, history, etc
* Extract out and optimize prediction process

# Presentation Materials

Video Link: https://youtu.be/eEptH_mVsG8

Powerpoint Presentation: https://github.com/lvolkmann/edgar/blob/master/documentation/IOT%20Final%20Project%20Presentation_2020.pptx

# Resources

I'd like to extend an incredible thank you to the people at pyimagesearch.com. Without their blog posts and starter code, the machine learning component of the project would have never come together.

https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/ 

https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

https://www.pyimagesearch.com/2018/04/09/how-to-quickly-build-a-deep-learning-image-dataset/

https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826



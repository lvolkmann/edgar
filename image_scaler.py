import PIL
from PIL import Image
import os

def scale_and_rotate(source, destination, basewidth = 1000): 

    img = Image.open(source)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img = img.rotate(-90)
    img.save(destination)

img_folder_path = '/home/pi/Development/edgar/face-recognition-opencv/dataset/landon_volkmann'
images = os.listdir(img_folder_path)
for image in images:
    image_path = os.path.join(img_folder_path, image)
    scale_and_rotate(image_path,image_path)
    

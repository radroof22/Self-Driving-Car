from cv2 import *

cam = VideoCapture(0)

test_name = "APl"
folder = "Images"

def take_picture(action, i):
    s, img = cam.read()
    if s:
        imwrite("{}/{}{}.jpg".format(folder, action, i), img)

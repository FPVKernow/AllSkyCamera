#RPi AllSkyCamera by T. Winterton 2025
from site import makepath
from picamera2 import Picamera2  # type: ignore
import time
import os
import os.path
import datetime

today = datetime.datetime.now() #creates object for today

filePath = '/home/tom-winterton/Documents/code_projects/2025/pi_allSkyCamera/captures/'


def main():
    todayDir()
    picam2 = Picamera2()
    picam2.start()
    imgCapture()
    time.sleep(10)


    def imgCapture():
        picam2.capture_file(os.path.join(dirNames(filePath), f"{today}.png"))
        print("image captured")

    def todayDir():#needs error handelling if dir already exists
            os.mkdir(f"/home/tom-winterton/Documents/code_projects/2025/pi_allSkyCamera/captures/{today.strftime("%Y-%m-%d")}") #creates directory with today's date YYYY-MM-DD


    def dirNames(path):
        filenames = os.listdir(path)
        max(filenames)

    main()
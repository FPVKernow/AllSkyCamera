from picamera2 import Picamera2, Preview

import datetime
now = datetime.datetime.now()

picam2 = Picamera2

picam2.start_and_capture_file(now.jpg)
import time
from picamera2 import Picamera2, Preview

picam2 = Picamera2()

picam2.start_preview(Preview.QTGL, x=400, y=100)

preview_config = picam2.create_preview_configuration(main={"size":(100,100)})

picam2.configure(preview_config)

picam2.start()
time.sleep(20)
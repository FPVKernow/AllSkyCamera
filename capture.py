import time
from picamera2 import Picamera2, Preview

picam2 = Picamera2()

picam2.start_preview(Preview.QTGL)

preview_config = picam2.create_preview_configuration(main={"size":(3040,3040)})
capture_config = picam2.create_still_configuration()

picam2.configure(preview_config)

picam2.start(capture_config)
time.sleep(20)
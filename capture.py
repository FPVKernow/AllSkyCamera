import time
from picamera2 import Picamera2, Preview

picam2 = Picamera2()

picam2.start_preview(Preview.QTLG)

preview_config = picam2.create_preview_configure(main={"size":(1000,1000)})

picam2.configure(preview_config)

picam2 = start()
time.sleep(20)
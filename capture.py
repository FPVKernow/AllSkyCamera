from time import sleep;
from picamera import Picamera; # type: ignore

camera = Picamera();
camera.resolution(3040,3040);
camera.start_preview();
sleep(2);

camera.capture('python.jpg');
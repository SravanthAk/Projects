import picamera

with picamera.PiCamera() as camera:
	camera.resolution=(640,480)
	camera.framerate=30
	for file_name in camera.record_sequence('/home/pi/Videos/video%03d.h264'%i for i in range(3)):
		print('Recording to %s' % file_name)
		camera.wait_recording(5)
		

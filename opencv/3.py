import picamera
import os
import psutil #process and system monitoring in python

MAX_FILES=999
DURATION=1
SPACE_LIMIT=80

file_root="/home/pi/Videos/"

if (psutil.disk_usage(".").percent>SPACE_LIMIT):
	print("WARNING: Low space!")
	exit()
with picamera.PiCamera() as camera:
	camera.resolution=(640,480)
	camera.framerate=30
	print("Searching files...")
	for i in range(1,MAX_FILES):
		file_number=i
		file_name=file_root+"video"+str(i).zfill(3)+".h264"
		exists=os.path.isfile(file_name)
		if not exists:
			print ("Search complete")
			break
	for file_name in camera.record_sequence(file_root+"video%03d.h264"%i for i in range(file_number,MAX_FILES)):
		print("Recording to %s"%file_name)
		camera.wait_recording(DURATION*60)
		if (psutil.disk_usage(".").percent>SPACE_LIMIT):
			print("WARNING: Low space!")
			break;

import cv2					# imports image processing
import time					# Used to measure execution time
start_time = time.time()	# begin time

image = cv2.imread("/home/jose/Downloads/obama1.jpg")	# reading jpg file inside download folder
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)		# resizes jpg file by 0.5(50%) uncomment to run
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	# color image to grey scale

cv2.imshow('Preview', gray_image)				# Creates a new window that show file that was read

print("Time to process --- %s seconds ---" % (time.time() - start_time))# outputs time for greyscaling

cv2.waitKey(0)					# Must keep these lines for image to show properly
cv2.destroyAllWindows()			# closes window after pressing a key e.g Space bar

cv2.imwrite("/home/jose/Desktop/obama1_greyscaled.jpg", gray_image) # saves converted grey image to desktop

print(gray_image.shape) # prints dimensions of grey image

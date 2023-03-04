import cv2					# imports image processing
import time					# Used to measure execution time
start_time = time.time()	# begin time

image = cv2.imread("/home/jose/Desktop/obama1_greyscaled.jpg")	#reading jpg file inside desktop folder
color_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)			# not perfect because grey scale
                                                                # impossible to recreate perfectly
                                                                
cv2.imshow('Preview', color_image)	# Creates a new window that show file that was read

print("Time to process --- %s seconds ---" % (time.time() - start_time))	# prints out execution time

cv2.waitKey(0)					# Must keep these lines for image to show properly
cv2.destroyAllWindows()			# closes window after pressing a key e.g Space bar

cv2.imwrite("/home/jose/Desktop/obama1_colorback.jpg", color_image)	# saves color back image to desktop

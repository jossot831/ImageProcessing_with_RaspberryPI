import cv2					# imports image processing
import time					# Used to measure execution time
start_time = time.time()	# begin time

image = cv2.imread("/home/jose/Downloads/obama1.jpg")# reading jpg file inside download folder

image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)	# resizes jpg file by 0.5(50%) uncomment to run

cv2.imshow('Preview', image)	# Creates a new window that show file that was read

print("Time to process --- %s seconds ---" % (time.time() - start_time))# outputs time for resizing

cv2.waitKey(0)					# Must keep these lines for image to show properly
cv2.destroyAllWindows()			# closes window after pressing a key e.g Space bar



dimensions = image.shape					# Prints out pixel dimensions of the image
print("Picture dimensions: ", dimensions)
cv2.imwrite("/home/jose/Desktop/obama1_resized.jpg", image)

(h, w, d)  = dimensions
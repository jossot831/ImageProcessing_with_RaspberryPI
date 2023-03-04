import cv2					# imports image processing
import time					# Used to measure execution time
start_time = time.time()	# begin time

image = cv2.imread("/home/jose/Downloads/obama1.jpg")	#reading jpg file inside download folder
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)		# resizes jpg file by 0.5(50%) uncomment to run
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	# grey scale the image


(h, w) = gray_image.shape[:2]		# calculates middle of grey image
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, 13, scale  =1.1)	# gives slight rotation, 
rotated_image = cv2.warpAffine(gray_image, M, (w, h))	# vary scale to have bigger effect

cv2.imshow('Rotated image', rotated_image)	# Creates a new window that show file that was read
print("Time to process --- %s seconds ---" % (time.time() - start_time))	#gives  execution time

cv2.waitKey(0)					# Must keep these lines for image to show properly
cv2.destroyAllWindows()			# closes window after pressing a key e.g Space bar

cv2.imwrite("/home/jose/Desktop/obama1_rotated.jpg", rotated_image) 	# saves processed image onto desktop
                                                                    


import cv2					# imports image processing
import time					# Used to measure execution time
start_time = time.time()	# begin time


image = cv2.imread("/home/jose/Downloads/obama1.jpg")	# reading jpg file inside download folder
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)		# resizes jpg file by 0.5(50%) uncomment to run
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	# color image to grey scale

(thresh, blackAndWhiteImage1) = cv2.threshold(gray_image, 20, 255, cv2.THRESH_BINARY) # threshold value = 20, All values ​​above 20 are assigned to 255
(thresh, blackAndWhiteImage2) = cv2.threshold(gray_image, 80, 255, cv2.THRESH_BINARY) # threshold value = 80, All values ​​above 80 are assigned to 255
(thresh, blackAndWhiteImage3) = cv2.threshold(gray_image, 160, 255, cv2.THRESH_BINARY) # threshold value = 160, All values ​​above 160 are assigned to 255
(thresh, blackAndWhiteImage4) = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY) # threshold value = 200, All values ​​above 200 are assigned to 255

cv2.imshow('Preview1', blackAndWhiteImage1)	# Creates a new window that show file that was read
cv2.imshow('Preview2', blackAndWhiteImage2)	# Creates a new window that show file that was read
cv2.imshow('Preview3', blackAndWhiteImage3)	# Creates a new window that show file that was read
cv2.imshow('Preview4', blackAndWhiteImage4)	# Creates a new window that show file that was read

print("Time to process --- %s seconds ---" % (time.time() - start_time)) # outputs time for greyscaling

cv2.waitKey(0)					# Must keep these lines for image to show properly
cv2.destroyAllWindows()			# closes window after pressing a key e.g Space bar

cv2.imwrite("/home/jose/Desktop/obama1_thresh1.jpg", blackAndWhiteImage1) #saves threshold images into desktop
cv2.imwrite("/home/jose/Desktop/obama1_thresh2.jpg", blackAndWhiteImage2)
cv2.imwrite("/home/jose/Desktop/obama1_thresh3.jpg", blackAndWhiteImage3)
cv2.imwrite("/home/jose/Desktop/obama1_thresh4.jpg", blackAndWhiteImage4)                          
                                                                    
print(gray_image.shape) # prints dimensions of gray image


#importing the opencv module  
import cv2  
  
# using imread('path') and 0 denotes read as  grayscale image  
img = cv2.imread(r"C:\Users\91935\OneDrive\Desktop\Opencv git hub\Topic 3 Reading images\images (3).jpeg",1)  
  
#This is using for display the image  
cv2.imshow('image',img)  
  
cv2.waitKey(0) # This is necessary to be required so that the image doesn't close immediately.  
#It will run continuously until the key press.  
cv2.destroyAllWindows()  
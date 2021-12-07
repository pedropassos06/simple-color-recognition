import cv2
import numpy as np

class ColorRecognition:

    def __init__(self):
        self.low_blue = np.array([161, 155, 84])
        self.high_blue = np.array([179, 255, 255])
    
    def detect(self):

        #start using camera device
        cap = cv2.VideoCapture(0)
        
        while True:

            success, frame = cap.read()
            
            #make sure camera device is working
            if success == False:
                print("Your camera device is not working properly")
                break
            
            #define a blue mask to start detecting blue objects
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            blue_mask = cv2.inRange(hsv_frame, self.low_blue, self.high_blue)

            #is esc is pressed, end program
            key = cv2.waitKey(1)
            if key == 27:
                break


cr = ColorRecognition()
cr.detect()



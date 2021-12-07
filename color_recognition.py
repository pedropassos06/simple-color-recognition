import cv2
import numpy as np

class ColorRecognition:

    def __init__(self):
        #blue HSV range
        self.low_blue = np.array([40, 85, 0])
        self.high_blue = np.array([121, 255, 255])
    
    def detect(self):

        #start using camera device
        cap = cv2.VideoCapture(0)
        
        while True:

            success, frame = cap.read()

            #make sure camera device is working
            if success == False:
                print("Your camera device is not working properly")
                break

            #blur the frame to avoid noise
            blur = cv2.GaussianBlur(frame, (5,5), 0)
            
            #create mask
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.low_blue, self.high_blue)

            #find and draw contours
            _, contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            for contour in contours:
                #ensure area is big enough
                area = cv2.contourArea(contour)

                if area > 60:
                    cv2.drawControus(frame, contour, -1, (0, 0, 255), 3)

            #display
            cv2.imshow("Frame", frame)
            cv2.imshow("Mask", mask)

            #is esc is pressed, quit detection process
            key = cv2.waitKey(1)
            if key == 27:
                break

        #close camera and application    
        cap.release()
        cv2.destroyAllWindows()

cr = ColorRecognition()
cr.detect()



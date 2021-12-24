import cv2
import numpy as np

class ColorRecognition:

    def __init__(self):

        #red HSV range
        self.low_red = np.array([150, 81, 0])
        self.high_red = np.array([180, 255, 255])

        #camera ID
        self.cam_ID = 0

        #kernel size
        self.kernel_size = (5,5)

        #thickness of contours
        self.cont_thickness = 3

        #colors
        self.green = (0, 255, 0)

        #min area
        self.min_area = 1000
    
    def detect(self):

        #start using camera device
        cap = cv2.VideoCapture(self.cam_ID)
        
        while True:

            success, frame = cap.read()

            #make sure camera device is working
            if success == False:
                print("Your camera device is not working properly")
                break

            #blur the frame to avoid noise
            blur = cv2.GaussianBlur(frame, self.kernel_size, 0)
            
            #create mask
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.low_red, self.high_red)

            #find and draw contours
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                #ensure area is big enough
                area = cv2.contourArea(contour)

                if area > self.min_area:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x,y), ( x+w, y+h ), self.green, self.cont_thickness)

            #display
            cv2.imshow("Frame", frame)

            #is esc is pressed, quit detection process
            key = cv2.waitKey(1)
            if key == 27:
                break

        #close camera and application    
        cap.release()
        cv2.destroyAllWindows()

cr = ColorRecognition()
cr.detect()
import cvzone 
import cv2
from cvzone.HandTrackingModule import HandDetector 


# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
 
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5) 


def getHandInfo(img):
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=False, flipType=True)
 
    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand = hands[0]  # Get the first hand detected
        lmList = hand["lmList"]  # List of 21 landmarks for the first hand
        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand)
        print(fingers)
        return fingers, lmList
    else:
        return None

canvas = None
img_combined = None

##coontinously get the frames of the webcam
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)

    if canvas is None:
        canvas = np.zero_like(img)

    info = getHandInfo(img) 
    if info:
        fingers, lmlist = info 
        print(fingers)
        prev_position = draw(info,previous_pos,canvas)
        img_combined= cv2.addweighted(img,0.85,canvas,0.15,0)

    ##display the image
    cv2.imshow(img)
    cv2.imshow(canvas)

    #display the image on the window 
    cv2.imshow("Image",img


def draw(info):
    fingers,lmlist = info
    #Resetting everytime we lost the fingure track
    current_pos = None
    
    #only the index fingure
    #the index finger needs the poinbt number 8 
    #we need only x and y 
    if fingers == [0,1,0,0,0]:
        if previous_pos is None : prev_pos = current_pos
        current_pos = lmlist[8][0:2]
        cv2,line(img,current_pos,(255,0,255),10)

    return current_pos

previous_pos = None 

 #keep the window open and update it each frame 
    cv2.waitkey(1)  

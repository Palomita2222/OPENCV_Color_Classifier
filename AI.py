import cv2
import TEST

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Get webcam frame
    ret, frame = cap.read()

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of blue color in RGB (for some reason)
    darker_light_blue = (50,50,100)
    lighter_light_blue = (100,255,255)


    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, darker_light_blue, lighter_light_blue)

    # Apply medianBlur to reduce noise, and GaussianBlur to clump color together (AKA better key detection)
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.GaussianBlur(mask, (5,5), 0)

    # Bitwise-AND mask and original image (only show colors through mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours of the blue objects
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 2000
    biggest_contour = None
    # Draw bounding boxes around the contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            biggest_contour = cnt
    if biggest_contour is not None:
        x, y, w, h = cv2.boundingRect(biggest_contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        TEST.test()

    

    # Show the webcam frame and the result
    #cv2.imshow("Webcam with overlay", frame)
    cv2.imshow("blue color mask", res)
    cv2.imshow("Webcam with overlay/s",cv2.drawContours(frame, contours, -1, (0,255,0), 3))

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()


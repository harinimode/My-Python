import cv2
import numpy as np

# Initialize global variables
clicked = False
r = g = b = xpos = ypos = 0

# Function to get RGB and HEX on mouse click
def pick_color(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Load image
img_path = r'C:\Users\HARSHITHA\Downloads\Python\my\sample_image3.jpg'  # Replace with your image file path
img = cv2.imread(img_path)
img = cv2.resize(img, (800, 600))  # Optional: Resize image for convenience

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', pick_color)

while True:
    display_img = img.copy()

    if clicked:
        # Create a color rectangle
        cv2.rectangle(display_img, (20, 20), (600, 60), (b, g, r), -1)

        # Prepare color values
        text = f'RGB = ({r}, {g}, {b})  HEX = #{r:02X}{g:02X}{b:02X}'
        cv2.putText(display_img, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
                    (255 - r, 255 - g, 255 - b), 2, cv2.LINE_AA)

    cv2.imshow('Image', display_img)

    # Break loop if ESC is pressed or window is closed
    if cv2.waitKey(20) & 0xFF == 27 or cv2.getWindowProperty('Image', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()

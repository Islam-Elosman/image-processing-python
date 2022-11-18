import cv2
import numpy as np

# Open the image.
img = cv2.imread("gray.jpg")

# Trying 3 gamma values.
for gamma in [3.0, 4.0, 5.0]:
    # Apply gamma correction.
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')

    # Save edited images.
    cv2.imshow('gamma_transformed' + str(gamma) + '.jpg', gamma_corrected) #photos appear one after another
    cv2.waitKey(0)
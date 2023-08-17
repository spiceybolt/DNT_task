import numpy as np
import cv2 as cv

impath = "thugduck.jpeg"

image = cv.imread(impath)

assert image is not None, "file could not be read, check with os.path.exists()"


# Convert the image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and enhance edge detection
blurred_image = cv.GaussianBlur(gray_image, (5, 5), 0)

# Apply Canny edge detection
sketch = cv.Canny(blurred_image, threshold1=30, threshold2=100)

cv.imwrite("thugducksketch.jpeg",sketch)
# Wait for a key press and close the windows
cv.waitKey(0)
cv.destroyAllWindows()

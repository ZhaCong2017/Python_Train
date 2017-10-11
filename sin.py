import cv2
import numpy as np
import math

width = 1000
height = 600
dims = 3
white = [255, 255, 255]

img = np.zeros((height, width, dims), np.uint8)

for i in range(width):
    j = 250 * math.sin(i * math.pi / 500) + 300
    img[int(j)][i] = white

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
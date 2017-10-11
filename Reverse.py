import random
import cv2
img = cv2.imread("b.jpg")
cv2.namedWindow("A")

white = [255, 255, 255]
black = [0, 0, 0]
print img.shape
raws, cols, dims = img.shape
for i in range(raws / 2):
    for j in range(cols):
        tmp = img[i, j].copy()
        img[i, j] = img[raws - 1 - i, j]
        img[raws - 1 - i, j] = tmp

# for i in range(5000):
#     x = random.randint(0, raws - 1)
#     y = random.randint(0, cols - 1)
#     img[x, y] = black
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
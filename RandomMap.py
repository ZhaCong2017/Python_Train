import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.new("RGBA", (1000, 1000), (255, 255, 255))

a = np.array(img.convert("L"))
raws, cols = a.shape
for i in range(1000):
    for j in range(1000):
        a[i, j] = random.randint(0, 255)

# for i in range(raws - 5):
#     for j in range(cols - 5):
#         if i % 100 == 0:
#             a[i: i + 5, j] = 1
#         if j % 100 == 0:
#             a[i, j + 5] = 1

plt.figure("Random")
plt.imshow(a, 'gray')
plt.axis('off')
plt.show()
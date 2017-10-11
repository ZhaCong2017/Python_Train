from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open("b.jpg").convert('L'))

plt.figure("b")
plt.imshow(img, 'gray')
plt.axis('off')
plt.show()
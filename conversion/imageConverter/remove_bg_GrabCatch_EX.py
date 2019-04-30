import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUR = 15
DILATE = 8
ERODE = 8
THRESH1 = 15
THRESH2 = 180
COLOR = (1.0, 1.0, 1.0)

type = 1

img_file = 'bg1.jpg'

# Defining main object rectangle
x1 = 0.2
x2 = 0.6
y1 = 0.2
y2 = 0.6

# Reading image
img = cv2.imread(img_file)

# Converting image to rgb
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Finding it's width and height
height, width = image_rgb.shape[:2]

# Marking rectangle considering main object to be within this rectangle.
rectangle = (int(width*x1), int(height*y1), int(width*x2), int(height*y2))

# Creating a mask
mask = np.zeros(image_rgb.shape[:2], np.uint8)

# Background mask
bgdModel = np.zeros((1, 65), np.float64)

# Foreground mask
fgdModel = np.zeros((1, 65), np.float64)

# Applying grab cut on the image using rectangle and mask
cv2.grabCut(image_rgb, mask, rectangle,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

# Creating another mask where mask=2
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

# Applying mask on the original image
image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]

# Converting image to grayscale
gray = cv2.cvtColor(image_rgb_nobg, cv2.COLOR_BGR2GRAY)

# Applying canny, dilate and erode to find lines, edges
edges = cv2.Canny(gray, THRESH1, THRESH2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

c_info = []
# Finding contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Creating a list of contour vertex and its area
for c in contours:
    c_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c),))

# Sorting all contours in descending order of their area.
c_info = sorted(c_info, key=lambda c: c[2], reverse=True)

# Finding max contour
max_contour = c_info[0]
image_mask = np.zeros(edges.shape)

# Applying convex polygon on the image using max contour
cv2.fillConvexPoly(image_mask, max_contour[0], (255))

# Smoothing the selected contour
image_mask = cv2.dilate(image_mask, None, iterations=DILATE)
image_mask = cv2.erode(image_mask, None, iterations=ERODE)

# Creating gaussian blur
image_mask = cv2.GaussianBlur(image_mask, (BLUR, BLUR), 0)
mask_stack = np.dstack([image_mask] * 3)
mask_stack = mask_stack.astype('float32') / 255.0
# Applying mask
img = img.astype('float32') / 255.0
masked = (mask_stack * img) + ((1 - mask_stack) * COLOR)
masked = (masked * 255).astype('uint8')
# Writing the converted image at specified path.
cv2.imwrite("output.jpg", masked)
plt.imshow(masked), plt.axis("off")
plt.show()

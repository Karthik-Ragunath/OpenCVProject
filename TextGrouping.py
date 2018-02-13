import cv2
import numpy as np
import array

originalImage = cv2.imread("/Users/karthik-5060/Documents/GitHub/EAST/demo_images/img_75.jpg")
copiedImage = originalImage.copy()
#print(copiedImage)
numberOfRows = len(copiedImage)
numberOfColumns = len(copiedImage[0])
print(numberOfRows)
print(numberOfColumns)
numpyImageArray = np.array(copiedImage)

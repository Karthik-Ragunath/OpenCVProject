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
print("Numpy array row length is %d." %(len(numpyImageArray)))
print("Numpy array column length is %d." %(len(numpyImageArray[0])))

newImageListBlack = [[0 for x in range(len(numpyImageArray[0]))] for x in range(len(numpyImageArray))]
newImageNumpyArrayBlack = np.array(newImageListBlack)
#print(newImageListBlack)
cv2.imwrite('BlackImage.jpg', newImageNumpyArrayBlack)
cv2.imshow("Black Image", newImageNumpyArrayBlack)

newImageListWhite = [[255 for x in range(len(numpyImageArray[0]))] for x in range(len(numpyImageArray))]
newImageNumpyArrayWhite = np.array(newImageListWhite)
#print(newImageNumpyArrayWhite)
cv2.imwrite('WhiteImage.jpg', newImageNumpyArrayWhite)
cv2.imshow("White Image", newImageNumpyArrayWhite)

fileData = []
with open("/Users/karthik-5060/Documents/TensorFlow/img_10.txt", "r") as line:
    lines = line.read().splitlines()
    for currentLine in lines:
        commaSeparatedList = currentLine.split(',')
        fileData.append(commaSeparatedList)

print(fileData) 

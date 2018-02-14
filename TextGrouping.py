import cv2
import numpy as np
import array

originalImage = cv2.imread("/Users/karthik-5060/Documents/GitHub/EAST/demo_images/img_2.jpg")
#originalImage = cv2.imread("/Users/karthik-5060/Documents/GitHub/EAST/demo_images/Hello_world_real.png")
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
#with open("/Users/karthik-5060/Documents/TensorFlow/Hello_world_real.txt", "r") as line:
with open("/Users/karthik-5060/Documents/TensorFlow/img_2.txt", "r") as line:
    lines = line.read().splitlines()
    for currentLine in lines:
        commaSeparatedList = currentLine.split(',')
        fileData.append(commaSeparatedList)

print(fileData)

numberOfWords = len(fileData)
leftTopX = []
leftTopY = []
rightTopX = []
rightTopY = []
rightBottomX = []
rightBottomY = []
leftBottomX = []
leftBottomY = []

for i in range(numberOfWords):
    leftTopX.append(fileData[i][0])
    leftTopY.append(fileData[i][1])
    rightTopX.append(fileData[i][2])
    rightTopY.append(fileData[i][3])
    rightBottomX.append(fileData[i][4])
    rightBottomY.append(fileData[i][5])
    leftBottomX.append(fileData[i][6])
    leftBottomY.append(fileData[i][7])

'''
print(leftTopX)
print(leftTopY)
print(rightTopX)
print(rightTopY)
print(rightBottomX)
print(rightBottomY)
print(leftBottomX)
print(leftBottomY)
'''

minMaxY = []
for i in range(numberOfWords):
    minY = leftTopY[i]
    if(rightTopY[i] < minY):
        minY = rightTopY[i]
    maxY = leftBottomY[i]
    if(rightBottomY[i] > maxY):
        maxY = rightBottomY[i]
    minYInt = int(minY)
    maxYInt = int(maxY)
    localMinMax = []
    localMinMax.append(minYInt)
    localMinMax.append(maxYInt)
    minMaxY.append(localMinMax)

print(minMaxY)

newImageListWhiteBlacked = [[255 for x in range(len(numpyImageArray[0]))] for x in range(len(numpyImageArray))]
for i in range(numberOfWords):
    #newImageListWhiteBlacked = [[0 for x in range(minMaxY[i][0], minMaxY[i][1])] for x in range(len(numpyImageArray))]
    #newImageListWhiteBlacked = [[0 for x in range(len(numpyImageArray[0]))] for x in range(minMaxY[i][0], minMaxY[i][1])]
    for x in range(minMaxY[i][0], minMaxY[i][1]):
        for y in range(len(numpyImageArray[0])):
            newImageListWhiteBlacked[x][y] = 0

newImageNumpyArrayWhiteBlacked = np.array(newImageListWhiteBlacked)
'''
print("Row Value Check")
print(newImageNumpyArrayWhiteBlacked[minMaxY[0][0], :])
'''
cv2.imwrite('WhiteBlackImage.jpg', newImageNumpyArrayWhiteBlacked)
cv2.imshow("White Black Image", newImageNumpyArrayWhiteBlacked)

whiteBlackImage = cv2.imread("/Users/karthik-5060/Documents/GitHub/OpenCVProject/WhiteBlackImage.jpg")
copiedWhiteBlackImage = whiteBlackImage.copy()
newImageNumpyArrayWhiteBlackedImgGray = cv2.cvtColor(copiedWhiteBlackImage,cv2.COLOR_BGR2GRAY);
ret, thresh = cv2.threshold(newImageNumpyArrayWhiteBlackedImgGray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

numberOfContours = len(contours)
print(numberOfContours)
print(contours)
cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imwrite('ContourImage.jpg', image)
cv2.imshow("Contour Image", image)
        

import cv2
import imutils


image = cv2.imread('cat1.jpg')

(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 50]
print(" R={}, G={}, B={}".format(R, G, B))

roi = image[70:160, 220:420]
cv2.imshow('ROI', roi)

resized = cv2.resize(image, (200, 200))
cv2.imshow('RESIZED', resized)

cv2.imshow('Image', image)
cv2.waitKey(0)
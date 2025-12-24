import cv2, os

img = cv2.imread(os.path.join(os.path.dirname(__file__), 'images', 'dog.jpg'))
cv2.imshow("Image Window", img)

key = cv2.waitKey(0)
print("Pressed key code:", key)

cv2.destroyAllWindows()
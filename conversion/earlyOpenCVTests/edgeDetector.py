import cv2

img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)
edged = cv2.Canny(blur, 600, 100)

cv2.imshow("res", edged);cv2.waitKey();cv2.destroyAllWindows()
cv2.imwrite("res.png", edged)

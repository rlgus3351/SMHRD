import cv2

img = cv2.imread("webcrwaling/image/cogi.png", cv2.IMREAD_COLOR)
gray_img = cv2.Canny(img, 0, 360)


save_path = "webcrwaling/image/test_coki.png"
cv2.imwrite(save_path, gray_img)
cv2.imshow("img", img)
cv2.imshow("gray_img", gray_img)
cv2.waitKey()
cv2.destroyAllWindows
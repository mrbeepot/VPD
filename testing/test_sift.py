import cv2
import sys

def main():
    img = cv2.imread('rait.png')
    sift = cv2.xfeatures2d.SIFT_create(500)
    kp = sift.detect(img, None)
    img = cv2.drawKeypoints(img, kp, img)
    cv2.imwrite('sift_keypoints.jpg', img)

main()
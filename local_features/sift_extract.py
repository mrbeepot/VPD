import cv2
from config import Config
import csv
import numpy as np


# def extract_sift_features(image, count):
#     sift = cv2.xfeatures2d.SIFT_create()
#     key_points, descriptors = sift.detectAndCompute(image, None)
#     print("desc" + str(descriptors))
#     csv_file_name = Config.destination_file_path_temp + str(count) + ".csv"
#     with open(csv_file_name, "w", newline="") as file:
#         w = csv.writer(file)
#         w.writerow(Config.sift_key_point_title)
#         for kp in key_points:
#             line = [str(kp.angle), str(kp.class_id), str(kp.octave), str(kp.pt), str(kp.response), str(kp.size)]
#             w.writerow(line)
#         file.close()


def extract_sift_key_points(image):
    sift = cv2.xfeatures2d.SIFT_create()
    key_points = sift.detect(image=image)
    return key_points


def extract_sift_descriptors(image):
    sift = cv2.xfeatures2d.SIFT_create()
    k, d = sift.detectAndCompute(image, None)
    return d


def extract_sift_keypoints_and_descriptors(image, limit):
    sift = cv2.xfeatures2d.SIFT_create(limit)
    k, d = sift.detectAndCompute(image, None)
    return k, d

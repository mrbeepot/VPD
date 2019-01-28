import cv2
from config import Config
import csv
import numpy as np


def extract_sift_features(frame, count):
    sift = cv2.xfeatures2d.SIFT_create()
    key_points, descriptors = sift.detectAndCompute(frame, None)
    print("desc" + str(descriptors))
    csv_file_name = Config.destination_file_path_temp + str(count) + ".csv"
    with open(csv_file_name, "w", newline="") as file:
        w = csv.writer(file)
        w.writerow(Config.sift_key_point_title)
        for kp in key_points:
            line = [str(kp.angle), str(kp.class_id), str(kp.octave), str(kp.pt), str(kp.response), str(kp.size)]
            w.writerow(line)
        file.close()

import numpy as np
import cv2
import pre_processing as pp
import csv
from config import Config


def main():
    frames = pp.get_frames(source_file_path=Config.source_file_path)
    count = 0
    for frame in frames:
        print("frame: " + str(count))
        sift = cv2.xfeatures2d.SIFT_create()
        key_points = sift.detect(frame, None)
        csv_file_name = Config.destination_file_path_temp + str(count) + ".csv"
        with open(csv_file_name, "w", newline="") as file:
            w = csv.writer(file)
            w.writerow(Config.sift_key_point_title)
            for kp in key_points:
                line = [str(kp.angle), str(kp.class_id), str(kp.octave), str(kp.pt), str(kp.response), str(kp.size)]
                w.writerow(line)
            file.close()

        # final_image = None
        # final_image = cv2.drawKeypoints(frame, key_points, final_image)
        # destination_file_path = destination_file_path_temp + str(count) + destination_image_extension
        # cv2.imwrite(destination_file_path, final_image)
        count += 1


main()
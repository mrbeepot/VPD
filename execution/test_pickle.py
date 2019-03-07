import cv2
import sys
import numpy as np
import pickle

def unpickle_keypoints(array):
    keypoints = []
    descriptors = []
    for point in array:
        temp_feature = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
        temp_descriptor = point[6]
        keypoints.append(temp_feature)
        descriptors.append(temp_descriptor)
    return keypoints, np.array(descriptors)


def main():
    keypoints_database = pickle.load(open("../picklefiles/keypoints_database.p", "rb"))
    # kp1, desc1 = unpickle_keypoints(keypoints_database[0])
    # kp2, desc2 = unpickle_keypoints(keypoints_database[1])

    for keypoints in keypoints_database:
        kp, desc = unpickle_keypoints(keypoints)
        print(kp)
        print(desc)
        print()


main()


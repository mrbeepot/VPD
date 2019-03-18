import cv2
import numpy as np
import pickle
import local_features as lf


def pickle_keypoints(keypoints, descriptors):
    i = 0
    temp_array = []
    for point in keypoints:
        temp = (point.pt, point.size, point.angle, point.response, point.octave,
        point.class_id, descriptors[i])
        i += 1
        temp_array.append(temp)
    return temp_array


def unpickle_keypoints(array):
    keypoints = []
    descriptors = []
    for point in array:
        temp_feature = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
        temp_descriptor = point[6]
        keypoints.append(temp_feature)
        descriptors.append(temp_descriptor)
    return keypoints, np.array(descriptors)


def generate_pickle_list(video_name, frames):
    temp_array = []
    count = 0
    for f in frames:
        k, d = lf.extract_sift_keypoints_and_descriptors(image=f, limit=500)
        temp = pickle_keypoints(k, d)
        temp_array.append(temp)
        count += 1
        print("\r",end="")
        print('Frames added to buffer for creating pickle file: ' + str(count), end="")
    with open("../picklefiles/video_"+str(video_name)+".p", "wb") as f:
        pickle.dump(temp_array, f)
        print('\nPickle file created')

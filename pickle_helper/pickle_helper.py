import cv2
import numpy as np
import pickle
import local_features as lf
import config


def pickle_keypoints(keypoints=None, descriptors=None):
    # assert keypoints is not None, "Please provide keyoints."
    # assert descriptors is not None, "Please provide descriptors."
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


def generate_pickle_list(video_name=None, frames=None, limit=config.LOCAL_FEATURES_IN_A_FRAME_LIMIT):
    assert video_name is not None, "Please provide name and extension of video file."
    assert frames is not None, "Please provide frames to process."
    assert len(frames) > 0, "Frame list is empty"
    temp_array = []
    count = 0
    video_name_without_ext = video_name.split(".")[0]
    assert video_name_without_ext is not "" or None, "Error fetching the video name."
    for f in frames:
        assert f is not None, "None type frame detected."
        k, d = lf.extract_sift_keypoints_and_descriptors(image=f, limit=limit)
        temp = pickle_keypoints(k, d)
        temp_array.append(temp)
# <<<<<<< HEAD
#         # print('new frame added to list')
#     print(len(temp_array))
#     pickle.dump(temp_array, open("../picklefiles/video_"+str(video_name)+".p", "wb"))
#     print('pickle file created')
# =======
        count += 1
<<<<<<< HEAD
        print("\r", end="")
        print('Frames added to buffer for creating pickle file: ' + str(count), end="")
    with open("../picklefiles/video_"+str(video_name)+".p", "wb") as f:
=======
        print("\r",end="")
        print('Frames added to buffer for creating pickle file: ' + str(count), end="\r")
    with open(config.PICKLE_FILES_DIR + str(video_name)+".p", "wb") as f:
>>>>>>> master
        pickle.dump(temp_array, f)
        print('\nPickle file created')
# >>>>>>> 40e08ba0eb738aa60c18a2c2ecb9bad99d78b793

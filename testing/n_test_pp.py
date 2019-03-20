import sys
sys.path.append("../")


import preprocessing as pp
import config

def test_preprocessing():
    # frames = pp.get_frames()
    # frames = pp.get_frames(config.VIDEO_DATASET_DIR)
    frames = pp.get_frames(config.VIDEO_DATASET_DIR + "2camerasfinal_512kb.mp4")


    # d = pp.get_video_duration(config.VIDEO_DATASET_DIR + "2camerasfinal_512kb.mp4")
    # print(d)


test_preprocessing()
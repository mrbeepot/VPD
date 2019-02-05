import preprocessing as pp
import local_features as lf
import cv2
import numpy

def test_sift_extract():
    video_source_file_path = "../dataset/videos/200_512kb.mp4"
    test_frames_file_path = "frames/"
    fps = 30
    width = 480
    height = 360
    frames = pp.get_frames(video_file_source_path=video_source_file_path, fps=fps, width=width, height=height)
    c = 0
    for f in frames:
        key_points = lf.extract_sift_key_points(image=f)
        descriptors = lf.extract_sift_descriptors(image=f)
        print(type(key_points), end=' ')
        print(type(descriptors))
        print(c, end=' ')
        if key_points is not None:
            print(len(key_points), end=' ')
        else:
            pass
        if descriptors is None:
            print("none")
        else:
            pass
        c += 1
    # print(len(key_points))
    # print(len(descriptors))


test_sift_extract()

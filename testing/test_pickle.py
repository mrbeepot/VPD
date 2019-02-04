import pickle
import preprocessing as pp
import local_features as lf


def test_pickling():
    video_source_file_path = "../dataset/videos/200_512kb.mp4"
    test_frames_file_path = "frames/"
    fps = 30
    width = 480
    height = 360
    frames = pp.get_frames(video_file_source_path=video_source_file_path, fps=fps, width=width, height=height)
    c = 0
    key_points = lf.extract_sift_key_points(image=frames[20])
    descriptors = lf.extract_sift_descriptors(image=frames[20])

    p = pickle.dumps(descriptors)
    print(len(p))

    d_new = pickle.loads(p)


test_pickling()

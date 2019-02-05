import database
import preprocessing as pp
import local_features as lf
import numpy


def insert_frames():
    video_file_name = "071404whoisthisman_512kb"
    video_source_file_path = "../dataset/videos/071404whoisthisman_512kb.mp4"
    test_frames_file_path = "frames/"
    fps = 30
    width = 480
    height = 360
    print("variables set.")
    print("fetching frames.")
    frames = pp.get_frames(video_file_source_path=video_source_file_path, fps=fps, width=width, height=height)
    print("\n\nfetched frames\n\n")
    c = 1
    kp_list = []
    d_list = []
    for f in frames:
        print("extracting features for frame : " + str(c))
        key_points = lf.extract_sift_key_points(image=f)
        if key_points is not None:
            # print(type(key_points))
            if len(key_points) > 500:
                key_points = key_points[:500]
                print(len(key_points))
        descriptors = lf.extract_sift_descriptors(image=f)
        if descriptors is not None:
            if numpy.shape(descriptors)[0] > 500:
                descriptors = descriptors[:500, :]
            print(type(descriptors))
            print(numpy.shape(descriptors))
        print("extracted features for frame : " + str(c))
        kp_list.append(key_points)
        d_list.append(descriptors)
        c += 1
    database.insert_frames_in_database(video_file_name=video_file_name, key_points=kp_list, descriptors=d_list)


insert_frames()

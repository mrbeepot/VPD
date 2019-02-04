import preprocessing
import cv2


def main():
    video_source_file_path = "../dataset/videos/200_512kb.mp4"
    test_frames_file_path = "frames/"
    fps = 30
    width = 480
    height = 360
    frames = preprocessing.get_frames(video_file_source_path=video_source_file_path, fps=fps, width=width, height=height)
    c = 0
    for frame in frames:
        cv2.imwrite(test_frames_file_path + str(c) + ".png", frame)
        c += 1


main()

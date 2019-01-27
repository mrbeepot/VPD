import numpy as np
import cv2
import time


def get_frames(source_file_path):
    capture = get_video_stream(source_file_path)
    frames = get_grayscale_frames(capture)
    return frames


def get_video_stream(source_file_path):
    assert type(source_file_path) is str, "video_file_name should be a string"
    capture = cv2.VideoCapture(source_file_path)
    capture.set(cv2.CAP_PROP_FPS, 1)
    return capture


def get_grayscale_frames(capture):
    assert type(capture) is cv2.VideoCapture, "capture parameter should be of type cv2.VideoCapture"
    frames = []
    count = 0
    while capture.isOpened():
        success, img = capture.read()
        if success is True and img is not None:
            if count % 15 == 0:
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                frames.append(gray)
            count += 1
        else:
            break
    return frames




import numpy as np
import sys
import os.path
import cv2


def __get_video_stream(video_file_source_path=None):
    video_capture = cv2.VideoCapture(video_file_source_path)
    return video_capture


def getFrame(video_capture, sec):
    video_capture.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    success, image = video_capture.read()
    if success:
        cv2.imwrite("outputs/frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file
    return success, image


def __build_frame_list(video_capture, req_fps, width, height):
    sec = 0
    frames = []

    # frame_rate = 0.5  # it will capture image in each second
    # success, image = getFrame(video_capture, sec)
    # while success:
    #     sec = sec + frame_rate
    #     sec = round(sec, 2)
    #     success, image = getFrame(video_capture, sec)
    #     if(success):
    #         image = image.astype('uint8')
    #         resized = __resize_frame(image=image, width=width, height=height, inter=cv2.INTER_AREA)
    #         gray = __convert_to_grayscale(resized)
    #         frames.append(gray)
    #         print("new frame captured")
    # print(len(frames))
    # return frames

    count = 0
    frame_count = 0
    fps = round(video_capture.get(cv2.CAP_PROP_FPS), 0)
    convert = int(fps / req_fps)
    print('fps of video: '+ str(fps))
    while video_capture.isOpened():
        success, image = video_capture.read()
        if success is True and image is not None:
            if count % convert == 0:
                resized = __resize_frame(image=image, width=width, height=height, inter=cv2.INTER_AREA)
                gray = __convert_to_grayscale(resized)
                # cv2.imwrite("outputs/frame " + str(count) + " sec.jpg", image)  # save frame as JPG file
                frames.append(gray)
                frame_count += 1
                print("\r",end="")

            count += 1
            # print("new frame captured")
        else:
            break
    print("Frame(s) captured: " + str(frame_count), end="")
    return frames


def __resize_frame(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    image = cv2.resize(image, dim, interpolation=inter)
    return image


def __convert_to_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def get_frames(video_file_source_path=None, req_fps=None, width=None, height=None):
    video_capture = __get_video_stream(video_file_source_path=video_file_source_path)
    print("Retrieving and preprocessing frames...")
    frames = __build_frame_list(video_capture=video_capture, req_fps=req_fps, width=width, height=height)
    print("\nCaptured all frames")
    return frames


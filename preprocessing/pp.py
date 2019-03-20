import cv2
from pathlib import Path
import config


def __get_video_stream(video_path=None):
    assert video_path is not None, "Please supply a video path"
    video_capture = cv2.VideoCapture(video_path)
    return video_capture


def __build_frame_list(video_capture=None,fps=config.FPS, width=config.WIDTH, height=config.HEIGHT, video_name=None):
    assert type(video_capture) is cv2.VideoCapture, "Incorrect object passed for video_capture"
    assert video_capture is not None, "Please provide a video_capture object (cv2.VideoCapture) with a video stream" 
    
    sec = 0
    frames = []
    count = 0
    frame_count = 0
    
    default_fps = round(video_capture.get(cv2.CAP_PROP_FPS), 0)
    convert = int(default_fps / fps)
    
    while video_capture.isOpened():
        success, image = video_capture.read()
        
        if success is True and image is not None:
            if count % convert == 0:
                resized = __resize_frame(image=image, width=width, height=height, inter=cv2.INTER_AREA)
                gray = __convert_to_grayscale(image=resized)
                # print(config.DEMO_FRAMES_DIR + video_name + str(frame_count) + ".png")
                cv2.imwrite(config.DEMO_FRAMES_DIR + video_name + str(frame_count) + ".png", resized)
                frames.append(gray)
                
                frame_count += 1
                print("\r", end="")
                print("Frame(s) captured: " + str(frame_count), end="")
            count += 1
            # print("new frame captured")
        else:
            break
    return frames


def __resize_frame(image=None, width=None, height=None, inter=cv2.INTER_AREA):
    assert image is not None, "Please provide an image"
    
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


def __convert_to_grayscale(image=None):
    assert image is not None, "Please provide an image"
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return gray


def get_frames(video_path=None, fps=config.FPS, width=config.WIDTH, height=config.HEIGHT):
    assert video_path is not None or "", "Please provide a video directory."
    assert Path(video_path).suffix in config.SUPPORTED_FILE_EXTENSIONS, ("File extension not supported")

    video_capture = __get_video_stream(video_path=video_path)
    print("Retrieving and preprocessing frames...")
    frames = __build_frame_list(video_capture=video_capture, fps=fps, width=width, height=height, video_name=Path(video_path).stem)
    
    print("\nCaptured all frames")
    
    return frames


def get_video_duration(video_path=None):
    assert video_path is not None, "Please supply a video path"

    video_capture = __get_video_stream(video_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    
    return duration


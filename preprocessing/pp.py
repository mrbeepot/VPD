import cv2


def __get_video_stream(video_file_source_path=None):
    video_capture = cv2.VideoCapture(video_file_source_path)
    return video_capture


def __build_frame_list(video_capture, fps, width, height):
    frames = []
    count = 0
    convert = int(fps / 2)
    while video_capture.isOpened():
        success, image = video_capture.read()
        if success is True and image is not None:
            if count % convert == 0:
                resized = __resize_frame(image=image, width=width, height=height, inter=cv2.INTER_AREA)
                gray = __convert_to_grayscale(resized)
                frames.append(gray)
            count += 1
        else:
            break
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


def get_frames(video_file_source_path=None, fps=None, width=None, height=None):
    video_capture = __get_video_stream(video_file_source_path=video_file_source_path)
    frames = __build_frame_list(video_capture=video_capture, fps=fps, width=width, height=height)
    return frames


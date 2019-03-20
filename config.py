import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEO_DATASET_DIR = ROOT_DIR + "/dataset/videos/"

PICKLE_FILES_DIR = ROOT_DIR + "/picklefiles/"

GOOD_VIDEOS_DATASET_DIR = ROOT_DIR + "/dataset/good_videos/"

DEMO_PROCESSED_VIDEOS_DIR = ROOT_DIR + "/dataset/processed_videos/"
DEMO_PROCESSED_ORIGINAL_VIDEO_DIR = ROOT_DIR + "/dataset/demo_main/"

FPS = 2
WIDTH = 480
HEIGHT = 360

SUPPORTED_FILE_EXTENSIONS = (
    ".mp4",
    ".avi",
    ".mkv"
)

LOCAL_FEATURES_IN_A_FRAME_LIMIT = 100

DEMO_FRAMES_DIR = ROOT_DIR + "/dataset/demo_frames/"

DEMO_PICKLE_FILES_DIR = "/picklefiles/demo/"

DEMO_FRAMES_DIR = ROOT_DIR + "/dataset/demo_frames/"
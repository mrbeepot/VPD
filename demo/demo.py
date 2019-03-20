import sys


sys.path.append("../")
import execution as ex
import config

def compare_same_video():
    original_video_name = "MAIN.mp4"
    ex.build_database_using_single_video(video_directory=config.DEMO_PROCESSED_VIDEOS_DIR, video_name=original_video_name, fps=6)
    ex.match_keypoints(video_dir=config.DEMO_PROCESSED_VIDEOS_DIR, video_name=original_video_name, pickle_database_path=config.PICKLE_FILES_DIR)

def compare_edited_video():
    original_video_name = "MAIN.mp4"
    ex.build_database_using_single_video(video_directory=config.DEMO_PROCESSED_VIDEOS_DIR, video_name=original_video_name, fps=6)
    query_video_name = "color shift.mp4"
    ex.match_keypoints(video_dir=config.DEMO_PROCESSED_VIDEOS_DIR, video_name=query_video_name, pickle_database_path=config.PICKLE_FILES_DIR)


def compare_different_video():
    pass

compare_edited_video()
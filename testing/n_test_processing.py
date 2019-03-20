import sys
sys.path.append("../")


import config
import execution


def test_processing():
    # execution.build_database_using_directory(video_directory=config.GOOD_VIDEOS_DATASET_DIR)
    # execution.build_database_using_directory()
    execution.build_database_using_single_video(video_name="2camerasfinal_512kb.mp4")

test_processing()
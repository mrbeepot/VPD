import sys
sys.path.append("../")


import config
import execution
import time



def test_processing():
    # execution.build_database_using_directory(video_directory=config.GOOD_VIDEOS_DATASET_DIR)
    # execution.build_database_using_directory()
    start = time.time()
    execution.build_database_using_single_video(video_directory=config.DEMO_PROCESSED_VIDEOS_DIR, video_name="MAIN.mp4")
    execution.build_database_using_single_video(video_directory=config.DEMO_PROCESSED_VIDEOS_DIR, video_name="Random movement.mp4")

    execution.match_keypoints_of_two_videos(video_one_dir=config.DEMO_PROCESSED_VIDEOS_DIR, video_one_name_without_ext="MAIN",video_one_pickle_dir=config.PICKLE_FILES_DIR, video_two_dir=config.DEMO_PROCESSED_VIDEOS_DIR, video_two_name_without_ext="Random movement", video_two_pickle_dir=config.PICKLE_FILES_DIR)
    print("Time required: " + str(time.time() - start))
    print("done")

test_processing()
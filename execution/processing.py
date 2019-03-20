import os
import preprocessing as pp
import time
import pickle_helper as ph
from pathlib import Path
import config
import sys


def build_database_using_directory(video_directory=config.VIDEO_DATASET_DIR, count=sys.maxsize, fps=config.FPS, width=config.WIDTH, height=config.HEIGHT):
	path_list = Path(video_directory).glob("**/*.mp4")
	current_count = 0
	print("Generating pickle files according to the given config...")
	for path in path_list:
		if current_count >= count:
			break
		else:
			print("\n\n\nCOUNT: " + str(current_count), end="\n\n\n")
			video_name = str(path.stem) + ".mp4"
			print("Processing video file: " + video_name)
			print("Preprocessing...")
			start = time.time()
			frames = pp.get_frames(video_path=str(path), fps=fps, width=width, height=height)
			duration = pp.get_video_duration(video_path=str(path))
			mid = time.time()
			print("Generating pickle dump...")
			ph.generate_pickle_list(video_name=str(path.stem), frames=frames)
			end = time.time()
			print("Duration of video is: " + str(duration) + " second(s).")
			print("Total frames used are: " + str(len(frames)))
			print("Time required for preprocessing is: " + str(mid - start))
			print("Time required for generating pickle file is: " + str(end - mid))
			print("Total time required for saving a video is: " + str(end-start))
			print("Average overall time required to process a frame is: " + str(duration / len(frames)))
		current_count += 1


<<<<<<< HEAD
main(video_source_directory_path="../dataset/videos/", count=13, fps=6, width=480, height=360)
=======
def build_database_using_single_video(video_directory=config.VIDEO_DATASET_DIR, video_name=None, fps=config.FPS, width=config.WIDTH, height=config.HEIGHT):
	assert video_name is not None, "Please provide a video name and extension."
	print("Generating pickle files according to the given config...")
	video_name_without_ext = os.path.split(video_name)[-1]
	print("Processing video file...")
	print("Preprocessing...")
	start = time.time()
	video_path = video_directory + video_name
	frames = pp.get_frames(video_path=video_path)
	duration = pp.get_video_duration(video_path=video_path)
	mid = time.time()
	print("Generating pickle dump...")
	ph.generate_pickle_list(video_name=video_name, frames=frames)
	end = time.time()
	print("Duration of video is: " + str(duration) + " second(s).")
	print("Total frames used are: " + str(len(frames)))
	print("Time required for preprocessing is: " + str(mid - start))
	print("Time required for generating pickle file is: " + str(end - mid))
	print("Total time required for saving a video is: " + str(end-start))
	print("Average overall time required to process a frame is: " + str(duration / len(frames)))


# build_database_using_directory(video_directory="../dataset/good_videos/", count=500, fps=2, width=480, height=360)
# build_database_using_single_video(video_directory="../dataset/good_videos/3girlsbaptism3_512kb.mp4", fps=2, width=480, height=360)
>>>>>>> master

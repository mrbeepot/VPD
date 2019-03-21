import sys
sys.path.append("../")
import preprocessing as pp
import time
import pickle_helper as ph
from pathlib import Path


def main(video_source_directory_path, count, fps, width, height):
	path_list = Path(video_source_directory_path).glob("**/*.mp4")
	current_count = 0
	print("Generating pickle files according to the given config...")
	for path in path_list:
		if current_count >= count:
			break
		else:
			print("\n\n\nCOUNT: " + str(current_count), end="\n\n\n")
			video_source_file_name = str(path.stem) + ".mp4"
			print("Processing video file: " + video_source_file_name)
			print("Preprocessing...")
			start = time.time()
			frames = pp.get_frames(video_file_source_path=str(path), req_fps=fps, width=width,height=height)
			mid = time.time()
			print("Time required for preprocessing is: " + str(mid - start))
			print("Generating pickle dump...");
			ph.generate_pickle_list(video_name=str(path.stem), frames=frames)
			end = time.time()
			print("Time required for generating pickle file is: " + str(end - mid) )
			print("Total time required for saving a video is: " + str(end-start))
		current_count += 1


main(video_source_directory_path="../dataset/videos/", count=19, fps=6, width=480, height=360)

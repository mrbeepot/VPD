import preprocessing as pp
import execution as exec

def build_database():
    exec.build_database_using_directory(video_source_directory_path="dataset/good_videos/", count=1000, fps=2, width=480, height=360)

def match_video(query_video_path):
    exec.match_keypoints(query_video_path=query_video_path, pickle_database_path="picklefiles/")

# build_database()
match_video("dataset/good_videos/24h_du_mans_le_film_512kb.mp4")
import preprocessing as pp
import time
import sys
import pickle_helper as ph

def main():
        print()
        for i in range(int(sys.argv[1]), int(sys.argv[2])):
                video_source_file_path = "../dataset/videos/"+str(i)+".mp4"
                fps=2
                width = 480
                height = 360
                start = time.time()

                frames = pp.get_frames(video_file_source_path=video_source_file_path, req_fps=fps, width=width, height=height)
                end = time.time()
                print(end - start)
                ph.generate_pickle_list(video_name=i,frames=frames)
                end = time.time()
                print(end-start)

main()
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
                capture_frames_start = time.time()

                print('----------video '+ str(i) + '-----' )
                frames = pp.get_frames(video_file_source_path=video_source_file_path, req_fps=fps, width=width, height=height)
                capture_frames_end = time.time()
                print('Time required to capture frames: ' + str(capture_frames_end - capture_frames_start))
                gen_pickle_start = time.time()
                ph.generate_pickle_list(video_name=i,frames=frames)
                gen_pickle_end = time.time()
                print('Time required to generate pickle file: '+str(gen_pickle_end-gen_pickle_start))
                print('Total time required for processing: ' + str((capture_frames_end - capture_frames_start) + (gen_pickle_end-gen_pickle_start)))
                print('\n')


main()

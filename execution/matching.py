import time
import cv2
import pickle_helper as ph
import pickle
import time
from pathlib import Path


def match_keypoints(pickle_source_directory_path, query_video, num_stored_videos):
    bf = cv2.BFMatcher()
    path_list = Path(pickle_source_directory_path).glob("**/*.p")
    query_keypoints_database = None
    for path in path_list:
        query_keypoints_database = pickle.load(open(str(path), "rb"))
        break
    count = 0
    for path in path_list:  # iterate for every video stored in db
        if count < num_stored_videos:
            count+=1
            pickle_source_file_name = str(path.stem) + ".p"
            print('-------------------- video '+str(pickle_source_file_name)+' start -----------------------------')

            last_match = 0  # keep track of last matched frame
            second_last_match = 0
            third_last_match = 0
            matched_keypoints = []  # add matched frames tupples

            stored_keypoints_database = pickle.load(open(str(path), "rb"))

            # iterate for every frame of query video
            for query_keypoints_index in range(len(query_keypoints_database)):
                kq, dq = ph.unpickle_keypoints(query_keypoints_database[query_keypoints_index])

                for stored_keypoints_index in range(third_last_match, len(stored_keypoints_database)):    # for every frame of stored video from last_match till end
                    ks, ds = ph.unpickle_keypoints(stored_keypoints_database[stored_keypoints_index])
                    # print(dq, ds)
                    # print('qframe: '+str(query_keypoints_index)+'  sframe: '+str(stored_keypoints_index)+' ', end='')
                    if len(dq) > 0 and len(ds) > 0:
                        matches = bf.match(dq, ds)

                        dist = [m.distance for m in matches]    # get match distance(difference) of each

                        thres_dist = (sum(dist) / len(dist)) * 0.7

                        # start_frame_match = time.time()

                        # keep only the reasonable matches
                        sel_matches = [m for m in matches if m.distance <= thres_dist]
                        end_frame_match = None
                        if len(sel_matches) >= (0.4 * len(stored_keypoints_database[stored_keypoints_index])):  # if greater than threhold
                            matched_keypoints.append((query_keypoints_index, stored_keypoints_index))
                            third_last_match = second_last_match
                            second_last_match = last_match
                            last_match = stored_keypoints_index+1

                            # end_frame_match = time.time()
                            # print('matched')

                            break
                        # else:
                        #     end_frame_match = time.time()
                        #     print('not matched')
                    # print(end_frame_match-start_frame_match)
            print('---video'+'-----', matched_keypoints)
            print(len(matched_keypoints))
            if len(matched_keypoints) > 10:
                print('Plagiarism Detected')
            else:
                print('Plagiarism not detected')
            print('-------------------- video ' + str(pickle_source_file_name) + ' end -----------------------------')
        else:
            break


def main():
    start = time.time()
    match_keypoints(pickle_source_directory_path='../picklefiles/', query_video=0, num_stored_videos=17)
    end = time.time()
    print(end - start)


main()

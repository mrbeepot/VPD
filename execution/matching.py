import time
import cv2
import pickle_helper as ph
import pickle
import time


def match_keypoints(query_video, num_stored_videos):
    bf = cv2.BFMatcher()
    query_keypoints_database = pickle.load(open("../picklefiles/video_"+str(query_video)+".p", "rb"))

    for i in range(num_stored_videos):  # iterate for every video stored in db
        print('-------------------- video '+str(i)+' start -----------------------------')

        last_match = 0  # keep track of last matched frame
        matched_keypoints = []  # add matched frames tupples

        stored_keypoints_database = pickle.load(open("../picklefiles/video_"+str(i)+".p", "rb"))

        # iterate for every frame of query video
        for query_keypoints_index in range(len(query_keypoints_database)):
            kq, dq = ph.unpickle_keypoints(query_keypoints_database[query_keypoints_index])

            for stored_keypoints_index in range(last_match, len(stored_keypoints_database)):    # for every frame of stored video from last_match till end
                ks, ds = ph.unpickle_keypoints(stored_keypoints_database[stored_keypoints_index])
                # print(dq, ds)
                print('qframe: '+str(query_keypoints_index)+'  sframe: '+str(stored_keypoints_index)+' ', end='')
                if len(dq) > 0 and len(ds) > 0:
                    matches = bf.match(dq, ds)

                    dist = [m.distance for m in matches]    # get match distance(difference) of each

                    thres_dist = (sum(dist) / len(dist)) * 0.5

                    # start_frame_match = time.time()

                    # keep only the reasonable matches
                    sel_matches = [m for m in matches if m.distance <= thres_dist]
                    end_frame_match = None
                    if len(sel_matches) >= (0.5 * len(stored_keypoints_database[stored_keypoints_index])):  # if greater than threhold
                        matched_keypoints.append((query_keypoints_index, stored_keypoints_index))
                        last_match = stored_keypoints_index+1
                        # end_frame_match = time.time()
                        print('matched')

                        break
                    else:
                        # end_frame_match = time.time()
                        print('not matched')
                # print(end_frame_match-start_frame_match)
        print('---video'+'1-----', matched_keypoints)
        if len(matched_keypoints) > 10:
            print('Plagiarism Detected')
        else:
            print('Plagiarism not detected')
        print('-------------------- video ' + str(i) + ' end -----------------------------')


def main():
    start = time.time()
    match_keypoints(query_video=0, num_stored_videos=3)
    end  = time.time()
    print(end - start)


main()

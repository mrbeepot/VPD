import time
import cv2
import pickle_helper as ph
import pickle
import time
from pathlib import Path
from . import processing 
import os
import config
from matplotlib import pyplot as plt

# def match_keypoints(query_video, num_stored_videos):
#     bf = cv2.BFMatcher()
#     query_keypoints_database = pickle.load(open("../picklefiles/video_"+str(query_video)+".p", "rb"))

#     for i in range(num_stored_videos):  # iterate for every video stored in db
#         print('-------------------- video '+str(i)+' start -----------------------------')

#         last_match = 0  # keep track of last matched frame
#         matched_keypoints = []  # add matched frames tupples

#         stored_keypoints_database = pickle.load(open("../picklefiles/video_"+str(i)+".p", "rb"))

#         # iterate for every frame of query video
#         for query_keypoints_index in range(len(query_keypoints_database)):
#             kq, dq = ph.unpickle_keypoints(query_keypoints_database[query_keypoints_index])

#             for stored_keypoints_index in range(last_match, len(stored_keypoints_database)):    # for every frame of stored video from last_match till end
#                 ks, ds = ph.unpickle_keypoints(stored_keypoints_database[stored_keypoints_index])
#                 # print(dq, ds)
#                 print('qframe: '+str(query_keypoints_index)+'  sframe: '+str(stored_keypoints_index)+' ', end='')
#                 if len(dq) > 0 and len(ds) > 0:
#                     matches = bf.match(dq, ds)

#                     dist = [m.distance for m in matches]    # get match distance(difference) of each

#                     thres_dist = (sum(dist) / len(dist)) * 0.5

#                     # start_frame_match = time.time()

#                     # keep only the reasonable matches
#                     sel_matches = [m for m in matches if m.distance <= thres_dist]
#                     end_frame_match = None
#                     if len(sel_matches) >= (0.5 * len(stored_keypoints_database[stored_keypoints_index])):  # if greater than threhold
#                         matched_keypoints.append((query_keypoints_index, stored_keypoints_index))
#                         last_match = stored_keypoints_index+1
#                         # end_frame_match = time.time()
#                         print('matched')

#                         break
#                     else:
#                         # end_frame_match = time.time()
#                         print('not matched')
#                 # print(end_frame_match-start_frame_match)
#         print('---video'+'1-----', matched_keypoints)
#         if len(matched_keypoints) > 10:
#             print('Plagiarism Detected')
#         else:
#             print('Plagiarism not detected')
#         print('-------------------- video ' + str(i) + ' end -----------------------------')


# def match_keypoints(video_dir=config.VIDEO_DATASET_DIR, video_name=None, pickle_database_path=config.PICKLE_FILES_DIR, fps=config.FPS):
#     bf = cv2.BFMatcher()

#     processing.build_database_using_single_video(video_directory=video_dir, video_name=video_name, fps=fps)
#     query_keypoints_database = pickle.load(open(pickle_database_path + video_name.split(".")[0] + ".p", "rb"))
    
#     path_list = Path(pickle_database_path).glob("**/*.p")
    
#     for path in path_list:
#         print("Matching with: " + str(path.stem))
        
#         last_match = 0 
#         matched_keypoints = []
        
#         stored_keypoints_database = pickle.load(open(str(path), "rb"))

#         for index in range(len(query_keypoints_database)):
#             kq, dq = ph.unpickle_keypoints(query_keypoints_database[index])
#             for stored_keypoints_index in range(last_match, len(stored_keypoints_database)):
#                 ks, ds = ph.unpickle_keypoints(stored_keypoints_database[index])   
#                 print('qframe: '+str(index)+'  sframe: '+str(stored_keypoints_index)+' ', end='')
#                 if len(dq) > 0 and len(ds) > 0:
#                     matches = bf.knnMatch(dq,ds, k=2)
#                     sel_matches = []
#                     for m, n in matches:
#                         if m.distance < 0.75 * n.distance:
#                             sel_matches.append([m])
#                     end_frame_match = None
#                     if len(sel_matches) >= (0.75 * len(stored_keypoints_database[stored_keypoints_index])):  # if greater than threhold
#                         matched_keypoints.append((index, stored_keypoints_index))
#                         last_match = stored_keypoints_index+1
#                         print('matched')
#                         break
#                     else:
#                         print('not matched')
#         if len(matched_keypoints) > 10:
#             print('Plagiarism Detected')
#         else:
#             print('Plagiarism not detected')

def match_keypoints_of_two_videos(video_one_dir, video_one_name_without_ext, video_two_dir, video_one_pickle_dir, video_two_name_without_ext, video_two_pickle_dir):
    v1_index = 0
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params,search_params)
    v1_pickle_file = video_one_pickle_dir + video_one_name_without_ext + ".p"
    v2_pickle_file = video_two_pickle_dir + video_two_name_without_ext + ".p"
    v1_pickle = pickle.load(open(v1_pickle_file,"rb"))
    v2_pickle = pickle.load(open(v2_pickle_file,"rb"))
    print()
    # print(len(v1_pickle))
    # print(len(v2_pickle))
    for v1_frame_data in v1_pickle:
        v2_index = 0
        print("New source frame: " + str(v1_index))
        k1, d1 = ph.unpickle_keypoints(v1_frame_data)
        v1_frame_image_path = config.DEMO_FRAMES_DIR + video_one_name_without_ext + str(v1_index) + ".png"
        v1_frame_image = cv2.imread(v1_frame_image_path)
        print("Match found for frames: ", end=" ")
        for v2_frame_data in v2_pickle:
            # print("New query frame: ", end="")
            k2, d2 = ph.unpickle_keypoints(v2_frame_data)
            # print(d2.shape)
            # print(d1.shape)
            if d2 is not None and d2.size > 0 and d1 is not None and d1.size > 0:
                matches = flann.knnMatch(d1, d2, k=2)
                matchesMask = [[0,0] for i in range(len(matches))]
                # ratio test as per Lowe's paper
                good_matches = 0
                for i,(m,n) in enumerate(matches):
                    if m.distance < 0.7*n.distance:
                        matchesMask[i]=[1,0]
                        good_matches += 1
                # for match in matchesMask:
                #     if match == [1,0]:
                #         print("Good Match found")
                # print(good_matches)
                if good_matches > 5:
                    print(str(v2_index) + ", ", end="")
                    draw_params = dict(matchColor = (0,255,0), singlePointColor = (255,0,0), matchesMask = matchesMask, flags = 0)
                    v2_frame_image_path = config.DEMO_FRAMES_DIR + video_two_name_without_ext + str(v2_index) + ".png"
                    v2_frame_image = cv2.imread(v2_frame_image_path)
                    result = None
                    result = cv2.drawMatchesKnn(v1_frame_image, k1 , v2_frame_image, k2, matches, None, **draw_params)
                    # print(type(result))
                    result_path = config.DEMO_FRAMES_DIR + "result___" + str(v1_index) + "___" + str(v2_index) + ".png"
                    plt.imsave(result_path, result)

            v2_index += 1
        v1_index += 1
        print()

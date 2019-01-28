import pre_processing as pp
from config import Config
import algorithm


def main():
    frames = pp.get_frames(source_file_path=Config.source_file_path)
    count = 0
    for frame in frames:
        print("frame: " + str(count))
        algorithm.extract_sift_features(frame, count)

        # final_image = None
        # final_image = cv2.drawKeypoints(frame, key_points, final_image)
        # destination_file_path = destination_file_path_temp + str(count) + destination_image_extension
        # cv2.imwrite(destination_file_path, final_image)
        count += 1


main()
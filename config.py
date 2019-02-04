class Config:

    source_directory_path = "videos/"
    source_file_name = "022404jobslost_512kb"
    source_file_extension = ".mp4"

    destination_directory_path = "frames/"
    destination_image_name = source_file_name + "_frame_"
    destination_image_extension = ".png"

    source_file_path = source_directory_path + source_file_name + source_file_extension
    destination_file_path_temp = destination_directory_path + destination_image_name

    sift_key_point_title = ["angle", "class_id", "octave", "pt", "response", "size"]

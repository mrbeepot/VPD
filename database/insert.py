import pickle
from .tables import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import numpy


def __create_database():
    engine_string = 'mysql+pymysql://root:@localhost/vpd'
    engine = create_engine(engine_string)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session


def __insert_video_in_database(session, video_file_name):
    new_video = Video(video_file_name=video_file_name)
    session.add(new_video)
    session.commit()


def __get_video_id(session, video_file_name):
    video = session.query(Video).filter_by(video_file_name=video_file_name).all()
    if len(video) is 1:
        print(video[0].id)
        return video[0].id


def __pickle_key_points(key_points):
    index = []
    for point in key_points:
        temp = (point.pt, point.size, point.angle, point.response, point.octave, point.class_id)
        index.append(temp)
    return pickle.dumps(index)


def __build_key_points(pickled_key_points):
    index = pickle.loads(pickled_key_points)
    kp = []
    for i in index:
        temp = cv2.KeyPoint(x=point[0][0], y=point[0][1], _size=point[1], _angle=point[2], _response=point[3],
                            _octave=point[4], _class_id=point[5])
        kp.append(temp)
    return kp


def insert_frames_in_database(video_file_name,  key_points, descriptors):
    session = __create_database()
    print("\n\ndb session created.")
    print("\n\ninserting video info in db.")
    __insert_video_in_database(session=session, video_file_name=video_file_name)
    print("\n\nvideo info inserted in db.")
    print("\n\nfetching video id from the database.")
    video_id = __get_video_id(session=session, video_file_name=video_file_name)
    print("video_id : " + str(video_id))
    count = 1
    for kp, d in zip(key_points, descriptors):
        if key_points is not None and descriptors is not None:
            if len(kp) > 0 and numpy.shape(d)[0] > 0 and numpy.shape(d)[1] > 0:
                print(len(kp))
                print(numpy.shape(d))
                pickled_kp = __pickle_key_points(kp)
                pickled_d = pickle.dumps(d)
                print("kp and d pickled successfully.")
                frame = Frame(video_id=video_id, frame_number=count, key_points=pickled_kp, descriptors=pickled_d)
                session.add(frame)
                session.commit()
                print(video_file_name + ": Frame no: " + str(count) + " inserted")
            else:
                print("dropping frame : " +str(count))
            count += 1








import pickle
from .tables import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def __create_database():
    engine_string = 'mysql+pymysql://root:@localhost/vpd'
    engine = create_engine(engine_string)
    Base.metadata.create_all(engine)
    return engine


def insert_video_in_database(video_file_name, key_points, descriptors):
    engine = __create_database()
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()
    new_video = Video(video_name=video_file_name)
    session.add(new_video)
    session.commit()


import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pickle
import preprocessing as pp
import local_features as lf

Base = declarative_base()

video_source_file_path = "../dataset/videos/200_512kb.mp4"
test_frames_file_path = "frames/"
fps = 30
width = 480
height = 360
frames = pp.get_frames(video_file_source_path=video_source_file_path, fps=fps, width=width, height=height)
c = 0
key_points = lf.extract_sift_key_points(image=frames[20])
descriptors = lf.extract_sift_descriptors(image=frames[20])

p = pickle.dumps(descriptors)


class Video(Base):
    __tablename__ = 'local_features_video'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    video_name = Column(LargeBinary(length=(2**32)-1), nullable=False)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('mysql+pymysql://root:@localhost/vpd1')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
new_video = Video(video_name=p)
session.add(new_video)
session.commit()

video = session.query(Video).first()

unpickle = pickle.loads(video.video_name)

print(type(unpickle))
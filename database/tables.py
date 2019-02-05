from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Video(Base):
    __tablename__ = "local_features_video"
    id = Column('id', Integer, primary_key=True)
    video_file_name = Column('video_file_name', String(255), unique=True, nullable=False)


class Frame(Base):
    __tablename__ = "local_features_frame"
    id = Column('id', Integer, primary_key=True)
    video_id = Column('video_id', Integer, ForeignKey(Video.id), nullable=False)
    frame_number = Column('frame_number', Integer, nullable=False)
    key_points = Column('key_points', LargeBinary((2**32)-1), nullable=False)
    descriptors = Column('descriptors', LargeBinary((2**32)-1), nullable=False)
    video = relationship(Video)

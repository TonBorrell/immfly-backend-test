from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Channel(Base):
    __tablename__ = "channel"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    language = Column(String)
    picture = Column(String)
    hasSubChannel = Column(Boolean, default=False)
    subchannel = Column(Integer, ForeignKey("channel.id"), default=0)
    hasSubContent = Column(Boolean, default=False)
    subcontent = Column(Integer, ForeignKey("content.id"), default=0)


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    files = Column(String)
    data = Column(String)
    rating = Column(Integer)

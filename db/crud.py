from sqlalchemy.orm import Session

from . import models, schemas


def get_channel(db: Session, channel_id: int):
    return db.query(models.Channel).filter(models.Channel.id == channel_id).first()


def get_all_channels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Channel).offset(skip).limit(limit).all()


def get_subchannel(db: Session, channel_id: int):
    if get_channel(db, channel_id).hasSubChannel:
        return get_channel(db, channel_id).subChannel


def create_channel(db: Session, channel: schemas.Channel):
    db_channel = models.Channel(
        title=channel.title,
        language=channel.language,
        picture=channel.picture,
        hasSubChannel=channel.hasSubChannel,
        subchannel=channel.subchannel,
        hasSubContent=channel.hasSubContent,
        subcontent=channel.subcontent,
    )
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel


def get_all_contents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Content).offset(skip).limit(limit).all()


def create_content(db: Session, content: schemas.Content):
    db_content = models.Content(
        files=content.files, data=content.data, rating=content.rating
    )
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

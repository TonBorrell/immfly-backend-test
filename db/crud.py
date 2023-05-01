from sqlalchemy.orm import Session

from . import models, schemas


def get_channel_by_id(db: Session, channel_id: int):
    return db.query(models.Channel).filter(models.Channel.id == channel_id).first()


def get_all_channels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Channel).offset(skip).limit(limit).all()


def delete_channels(db: Session):
    channels = get_all_channels(db)
    for channel in channels:
        db.delete(channel)
        db.commit()

    return "Done"


def get_subchannel(db: Session, channel_id: int):
    if get_channel_by_id(db, channel_id).hasSubChannel:
        return get_channel_by_id(db, channel_id).subChannel


def get_all_subchannels(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(models.Channel).offset(skip).limit(limit).all()
    all_subchannels = []
    for channel in result:
        if channel.hasSubChannel:
            all_subchannels.append(channel)

    return all_subchannels


def get_subchannels_by_id(db: Session, channel_id: int):
    channel = get_channel_by_id(db, channel_id)
    if channel.hasSubChannel:
        return get_channel_by_id(db, channel.subchannel)


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


def relate_one_channel_with_subchannel(
    db: Session, channel_id: int, subchannel_id: int
):
    channel = get_channel_by_id(db, channel_id)
    if not channel.hasSubChannel:
        channel.hasSubChannel = True
    channel.subchannel = subchannel_id
    db.commit()

    return channel


def relate_one_channel_with_content(db: Session, channel_id: int, content_id: int):
    channel = get_channel_by_id(db, channel_id)
    if not channel.hasSubContent:
        channel.hasSubContent = True
    channel.subcontent = content_id
    db.commit()

    return channel


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


def delete_contents(db: Session):
    contents = get_all_contents(db)
    for content in contents:
        db.delete(content)
        db.commit()

    return "Done"

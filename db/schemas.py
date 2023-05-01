from pydantic import BaseModel


class ChannelBase(BaseModel):
    id: int


class ChannelCreate(ChannelBase):
    pass


class Channel(ChannelBase):
    title: str
    language: str
    picture: str
    hasSubChannel: bool
    subchannel: int | None = None
    hasSubContent: bool
    subcontent: int | None = None

    class Config:
        orm_mode = True


class ContentBase(BaseModel):
    id: int


class ContentCreate(ContentBase):
    pass


class Content(ContentBase):
    files: str
    data: str
    rating: int

    class Config:
        orm_mode = True

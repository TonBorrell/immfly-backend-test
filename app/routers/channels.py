from fastapi import APIRouter, HTTPException, Request, Depends
from sqlalchemy.orm import Session

from db import crud, schemas
from db.functions import get_db

router = APIRouter(
    prefix="/api/v1/channels",
    tags=["channels"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def get_all_channels(db: Session = Depends(get_db)):
    return crud.get_all_channels(db=db)


@router.get("/{channel_id}/")
async def get_channel_by_id(channel_id: int, db: Session = Depends(get_db)):
    channel = crud.get_channel_by_id(db=db, channel_id=channel_id)
    if channel is not None:
        return channel
    else:
        raise HTTPException(status_code=404, detail="Channel not found")


@router.post("")
async def create_channel(channel: schemas.Channel, db: Session = Depends(get_db)):
    return crud.create_channel(db=db, channel=channel)


@router.delete("")
async def delete_all_channels(db: Session = Depends(get_db)):
    return crud.delete_channels(db=db)

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


@router.post("")
async def create_channel(channel: schemas.Channel, db: Session = Depends(get_db)):
    return crud.create_channel(db=db, channel=channel)

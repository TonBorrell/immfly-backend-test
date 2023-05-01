from fastapi import APIRouter, HTTPException, Request, Depends
from sqlalchemy.orm import Session

from db import crud, schemas
from db.functions import get_db

router = APIRouter(
    prefix="/api/v1/subchannels",
    tags=["subchannels"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def get_all_subchannels(db: Session = Depends(get_db)):
    return crud.get_all_subchannels(db=db)


@router.get("/{channel_id}/")
async def get_subchannel_by_id(channel_id: int, db: Session = Depends(get_db)):
    channel = crud.get_subchannels_by_id(db=db, channel_id=channel_id)
    if channel is not None:
        return channel
    else:
        raise HTTPException(status_code=404, detail="Channel not found")


@router.post("")
async def create_subchannel_relation(
    channel_id: int, subchannel_id: int, db: Session = Depends(get_db)
):
    return crud.relate_one_channel_with_subchannel(
        db=db, channel_id=channel_id, subchannel_id=subchannel_id
    )

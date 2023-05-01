from fastapi import APIRouter, HTTPException, Request, Depends
from sqlalchemy.orm import Session

from db import crud, schemas
from db.functions import get_db

router = APIRouter(
    prefix="/api/v1/content",
    tags=["content"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def get_all_contents(db: Session = Depends(get_db)):
    return crud.get_all_contents(db=db)


@router.post("")
async def create_content(content: schemas.Content, db: Session = Depends(get_db)):
    return crud.create_content(db=db, content=content)


@router.delete("")
async def delete_all_contents(db: Session = Depends(get_db)):
    return crud.delete_contents(db=db)


@router.post("-relation")
async def create_content_relation(
    channel_id: int, content_id: int, db: Session = Depends(get_db)
):
    return crud.relate_one_channel_with_content(
        db=db, channel_id=channel_id, content_id=content_id
    )

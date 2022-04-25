from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.scores as crud
from src.auth.jwthandler import get_current_user
from src.schemas.scores import ScoreOutSchema, ScoreInSchema, UpdateScore
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/scores",
    response_model=List[ScoreOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_scores():
    return await crud.get_scores()


@router.get(
    "/score/{score_id}",
    response_model=ScoreOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_score(score_id: int) -> ScoreOutSchema:
    try:
        return await crud.get_score(score_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Score does not exist",
        )

@router.get(
    "/score/by_user/{user_id}",
    response_model=ScoreOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_score_by_user(user_id: int) -> ScoreOutSchema:
    try:
        return await crud.get_score_by_user(user_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Score does not exist",
        )


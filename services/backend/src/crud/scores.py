from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Scores
from src.schemas.scores import ScoreOutSchema
from src.schemas.token import Status

async def create_score(user) -> ScoreOutSchema:
    score_dict = []
    score_dict["user"] = user.id
    score_obj = await Scores.create(**score_dict)
    return await ScoreOutSchema.from_tortoise_orm(score_obj)


async def update_score(user, score, current_user) -> ScoreOutSchema:
    try:
        db_score = await ScoreOutSchema.from_queryset_single(Scores.get(user=user))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Score for {user} not found")

    if db_score.author.id == current_user.id:
        await Scores.filter(id=user).update(**score.dict(exclude_unset=True))
        return await ScoreOutSchema.from_queryset_single(Scores.get(id=user))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")

async def get_score(score_id) -> ScoreOutSchema:
    return await ScoreOutSchema.from_queryset_single(Scores.get(id=score_id))    

async def get_score_by_user(user_id) -> ScoreOutSchema:
    return await ScoreOutSchema.from_queryset_single(Scores.get(user=user_id))        
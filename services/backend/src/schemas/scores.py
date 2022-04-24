from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Scores


ScroreInSchema = pydantic_model_creator(
    Scores, name="ScroreIn", exclude=["user"], exclude_readonly=True)
ScroreOutSchema = pydantic_model_creator(
    Scores, name="Scrore", exclude =[
      "modified_at", "user.password", "user.created_at", "user.modified_at"
    ]
)


class UpdateScrore(BaseModel):
    points: Optional[int]

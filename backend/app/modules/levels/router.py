from fastapi import APIRouter

from app.modules.levels.models import Level, LevelCreate, LevelUpdate
from app.modules.levels.service import create_level, list_levels, update_level

router = APIRouter()


@router.get("", response_model=list[Level])
def get_levels() -> list[Level]:
    return list_levels()


@router.post("", response_model=Level, status_code=201)
def post_level(payload: LevelCreate) -> Level:
    return create_level(payload)


@router.patch("/{level_id}", response_model=Level)
def patch_level(level_id: int, payload: LevelUpdate) -> Level:
    return update_level(level_id, payload)

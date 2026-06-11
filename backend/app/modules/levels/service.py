from fastapi import HTTPException

from app.core.store import store
from app.modules.levels.models import Level, LevelCreate, LevelUpdate


def list_levels() -> list[Level]:
    return [Level(**level) for level in sorted(store.levels.values(), key=lambda x: x["min_points"])]


def create_level(payload: LevelCreate) -> Level:
    level_id = store.next_id(store.levels)
    level = {"id": level_id, **payload.model_dump()}
    store.levels[level_id] = level
    return Level(**level)


def update_level(level_id: int, payload: LevelUpdate) -> Level:
    existing = store.levels.get(level_id)
    if not existing:
        raise HTTPException(status_code=404, detail="会员等级不存在")
    updates = payload.model_dump(exclude_unset=True)
    existing.update(updates)
    return Level(**existing)


def get_level(level_id: int) -> Level:
    level = store.levels.get(level_id)
    if not level:
        raise HTTPException(status_code=404, detail="会员等级不存在")
    return Level(**level)


def calculate_level_for_points(points: int) -> Level | None:
    sorted_levels = sorted(store.levels.values(), key=lambda x: x["min_points"], reverse=True)
    for level in sorted_levels:
        if points >= level["min_points"]:
            return Level(**level)
    return None

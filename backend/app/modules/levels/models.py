from pydantic import BaseModel, Field


class LevelBase(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    min_points: int = Field(ge=0)
    discount: float = Field(gt=0, le=1)
    benefits: list[str] = []


class LevelCreate(LevelBase):
    pass


class LevelUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=20)
    min_points: int | None = Field(default=None, ge=0)
    discount: float | None = Field(default=None, gt=0, le=1)
    benefits: list[str] | None = None


class Level(LevelBase):
    id: int

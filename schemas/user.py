from schemas.base import AbstractModel


class User(AbstractModel):
    id: int
    name: str
    x: float
    y: float

    class Config:
        orm_mode = True


class UserRadius(User):
    radius: float

    class Config:
        orm_mode = True

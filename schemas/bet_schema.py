from pydantic import BaseModel

class BetCreate(BaseModel):
    user_id: int
    amount: int
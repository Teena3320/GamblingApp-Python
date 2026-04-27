from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str
    full_name: str | None = None
    email: str | None = None
    initial_stake: float
    win_threshold: float
    loss_threshold: float
    min_required_stake: float

    def validate_stake(self):
        if self.initial_stake < self.min_required_stake:
            raise ValueError("Initial stake is below minimum required stake")

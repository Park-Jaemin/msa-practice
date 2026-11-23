from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from trade.models import ListingStatus


class CreateListing(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    description: str | None = None
    price: int = Field(gt=0)


class ListingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    price: int
    seller_id: int
    status: ListingStatus
    created_at: datetime

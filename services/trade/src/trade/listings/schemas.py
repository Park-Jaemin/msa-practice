from datetime import datetime
from enum import StrEnum
from zoneinfo import ZoneInfo

from pydantic import BaseModel, Field


class ListingStatus(StrEnum):
    on_sale = "ON_SALE"
    sold_out = "SOLD_OUT"


class Listing(BaseModel):
    id: int
    title: str
    description: str | None
    price: int
    seller_id: int
    status: ListingStatus = ListingStatus.on_sale
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul"))
    )


class CreateListing(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    description: str | None = None
    price: int = Field(gt=0)

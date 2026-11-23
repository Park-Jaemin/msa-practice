from typing import Annotated

from fastapi import APIRouter, Depends, Header
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from trade.db import get_session
from trade.listings.schemas import CreateListing, ListingResponse
from trade.models import Listing, ListingStatus

router = APIRouter(prefix="/listings", tags=["listings"])
SessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.get("", response_model=list[ListingResponse])
async def get_listings(session: SessionDep):
    return await session.scalars(select(Listing).where(Listing.status == ListingStatus.ON_SALE))


@router.get("/{listing_id}", response_model=ListingResponse)
async def get_listing(listing_id: int, session: SessionDep):
    return await session.get_one(Listing, listing_id)


@router.post("", response_model=ListingResponse, status_code=201)
async def create_listing(model: CreateListing, x_user_id: Annotated[int, Header()], session: SessionDep):
    listing = Listing(title=model.title, description=model.description, price=model.price, seller_id=x_user_id)
    session.add(listing)
    await session.commit()
    return listing

from typing import Annotated

from fastapi import APIRouter, Header, HTTPException

from trade.listings.schemas import CreateListing, Listing, ListingStatus

router = APIRouter(prefix="/listings", tags=["listings"])

listings: dict[int, Listing] = {
    1: Listing(id=1, title="1번", description="1번 설명", price=1000, seller_id=1),
    2: Listing(id=2, title="2번", description="2번 설명", price=2000, seller_id=2),
    3: Listing(id=3, title="3번", description="3번 설명", price=3000, seller_id=3),
}


@router.get("", response_model=list[Listing])
async def get_listings():
    return [l for l in listings.values() if l.status == ListingStatus.on_sale]


@router.get("/{listing_id}", response_model=Listing)
async def get_listing(listing_id: int):
    if (listing := listings.get(listing_id)) is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing


@router.post("", response_model=Listing, status_code=201)
async def create_listing(model: CreateListing, x_user_id: Annotated[int, Header()]):
    new_id = len(listings) + 1
    listing = Listing(
        id=new_id,
        title=model.title,
        description=model.description,
        price=model.price,
        seller_id=x_user_id,
    )
    listings[listing.id] = listing
    return listing

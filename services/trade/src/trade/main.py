from fastapi import FastAPI
from sqlalchemy.exc import NoResultFound

from trade.exception import not_found_handler
from trade.listings.router import router as listings_router

app = FastAPI()
app.include_router(listings_router)
app.add_exception_handler(NoResultFound, not_found_handler)  # type: ignore


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import DBAPIError, NoResultFound

from trade.db import SessionDep
from trade.exception import not_found_handler
from trade.listings.router import router as listings_router

app = FastAPI()
app.include_router(listings_router)
app.add_exception_handler(NoResultFound, not_found_handler)  # type: ignore


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/readyz")
async def readyz(session: SessionDep):
    try:
        await session.execute(text("SELECT 1"))
    except (DBAPIError, OSError) as e:
        return JSONResponse(status_code=503, content={"detail": str(e)})
    return {"status": "ok"}

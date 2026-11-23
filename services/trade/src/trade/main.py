from fastapi import FastAPI

from trade.listings.router import router as listings_router

app = FastAPI()
app.include_router(listings_router)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

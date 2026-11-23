from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import NoResultFound


async def not_found_handler(_request: Request, _exc: NoResultFound):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"detail": "Not found"})

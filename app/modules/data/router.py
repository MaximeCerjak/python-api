from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.deps import require_bearer_token

router = APIRouter(prefix="/data", tags=["data"])

class Item(BaseModel):
    id: str
    payload: dict

@router.post("/echo", dependencies=[Depends(require_bearer_token)])
async def data_echo(item: Item):
    return {"received": item.model_dump()}

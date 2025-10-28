from fastapi import APIRouter, Depends
from app.core.deps import require_bearer_token, require_api_token

router = APIRouter(prefix="/ai", tags=["ai"])

@router.get("/echo", dependencies=[Depends(require_bearer_token)])
async def ai_echo(text: str):
    return {"input": text, "output": text.upper()}

@router.post("/internal/refresh-cache", dependencies=[Depends(require_api_token)])
async def refresh_cache():
    return {"refreshed": True}

from fastapi import Header, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth import AuthService
from .config import settings

bearer_scheme = HTTPBearer(auto_error=False)

async def require_bearer_token(creds: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if not creds:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization header")
    AuthService.verify_token(creds.credentials)
    return True

async def require_api_token(x_api_token: str | None = Header(default=None, alias="x-api-token")):
    if not settings.API_TOKEN or x_api_token != settings.API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API token")
    return True

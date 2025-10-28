from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, status
from .config import settings

class AuthService:
    @staticmethod
    def create_token(subject: str, minutes: int | None = None) -> str:
        expire = datetime.utcnow() + timedelta(minutes=minutes or settings.JWT_EXPIRE_MINUTES)
        payload = {"sub": subject, "exp": expire}
        return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALG)

    @staticmethod
    def verify_token(token: str) -> dict:
        try:
            return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALG])
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

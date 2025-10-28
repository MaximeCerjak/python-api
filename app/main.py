import logging
import pkgutil, importlib, inspect
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.security import SecurityHeadersMiddleware
from app.core.auth import AuthService

app = FastAPI(title=settings.APP_NAME)

# Middleware sécurité + CORS
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auto-import des routers dans app.modules
def include_all_routers(app, base_package: str):
    package = importlib.import_module(base_package)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        try:
            module = importlib.import_module(f"{base_package}.{module_name}.router")
            for _, obj in inspect.getmembers(module):
                if hasattr(obj, 'routes'):
                    app.include_router(obj)
        except ModuleNotFoundError:
            pass

include_all_routers(app, "app.modules")

@app.get("/auth/dev-token")
async def dev_token(subject: str = "tester"):
    return {"access_token": AuthService.create_token(subject)}
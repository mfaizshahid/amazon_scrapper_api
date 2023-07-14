from fastapi import APIRouter

from app.routers import auth

router = APIRouter()
router.include_router(auth.auth_router)

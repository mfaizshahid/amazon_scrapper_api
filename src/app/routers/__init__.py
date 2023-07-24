from fastapi import APIRouter

from app.routers import auth, admin
router = APIRouter()
router.include_router(auth.auth_router)
router.include_router(admin.admin_router)

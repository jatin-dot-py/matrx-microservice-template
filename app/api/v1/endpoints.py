# File: app/api/v1/endpoints.py
import logging

from fastapi import APIRouter

from core import settings

router = APIRouter()
logger = logging.getLogger("app")


@router.get("/", tags=["v1"])
async def root():
    """Root endpoint"""
    logger.debug("Root endpoint called")
    return {
        "message": f"Welcome to {settings.APP_NAME} API",
        "version": settings.APP_VERSION,
        "docs": f"{settings.API_PREFIX}/docs"
    }



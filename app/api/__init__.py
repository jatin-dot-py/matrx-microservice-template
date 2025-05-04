# app\api\__init__.py
import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from matrx_utils import vcprint
from matrx_utils.core.task_queue import get_task_queue

from app.api.v1 import create_v1_app
from core import settings

logger = logging.getLogger('app')


def create_app() -> FastAPI:
    """Create and configure the FastAPI application with multiple API versions"""

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # --- startup block ---

        logger.info("FastAPI startup complete.")
        task_queue = get_task_queue()
        logger.info("[create_app] Task Queue Initialized.")

        # Startup related things go here.
        ##################################

        vcprint("[AI DREAM] All Core Services Starting...", color="green")
        # Initialize scraper
        # Initialize AI MODEL Manager
        # Initialize more stuff

        yield
        # --- shutdown block ---
        logger.info("Shutting down gracefully...")
        await task_queue.shutdown()
        logger.info("Task Queue Shutdown complete.")

    # Main app - no docs at root level
    main_app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="FastAPI Microservice with Multiple API Versions",
        docs_url=None,  # Disable default /docs
        redoc_url=None,  # Disable default /redoc,
        lifespan=lifespan
    )

    # Create API v1 sub-app
    v1_app = create_v1_app()

    # Create API v2 sub-app
    # v2_app = create_v2_app()

    # Mount the API versions at their respective paths
    main_app.mount("/api/v1", v1_app)

    # main_app.mount("/api/v2", v2_app)

    @main_app.get("/", include_in_schema=False)
    async def root():
        return {
            "message": f"Welcome to {settings.APP_NAME} API",
            "version": settings.APP_VERSION,
            "latest_docs": "/api/v1/docs",
            "v1_docs": "/api/v1/docs",
            # "v2_docs": "/api/v2/docs"
        }

    # Add logging middleware
    @main_app.middleware("http")
    async def log_requests(request, call_next):
        logger = logging.getLogger("app")
        start_time = time.time()
        path = request.url.path
        method = request.method

        logger.info(f"Request started: {method} {path}")

        try:
            response = await call_next(request)
            process_time = (time.time() - start_time) * 1000
            status_code = response.status_code

            logger.info(f"Request completed: {method} {path} - Status: {status_code} - Time: {process_time:.2f}ms")
            response.headers["X-Process-Time"] = f"{process_time:.2f}ms"
            return response
        except Exception as e:
            logger.error(f"Request failed: {method} {path} - Error: {str(e)}", exc_info=True)
            raise

    return main_app

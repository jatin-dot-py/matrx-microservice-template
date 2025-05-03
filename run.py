# run.py
import uvicorn
from core import settings
from matrx_utils import vcprint

if __name__ == "__main__":
    vcprint(
        f"Starting {settings.APP_NAME} v{settings.APP_VERSION} env={settings.ENVIRONMENT} debug={settings.DEBUG}",
        color="bright_yellow"
    )
    uvicorn.run(
        "core.app:app",  # Pass the app object directly
        host="127.0.0.1",
        port=settings.PORT,
        reload=False
    )
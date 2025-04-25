import logging
from dotenv import load_dotenv
load_dotenv()
import core.system_logger
from matrx_utils import vcprint
vcprint("[RUN.PY] Loaded environment variables", color="green")

import uvicorn
from app.api import create_app
from core import settings
from socketio import ASGIApp
from core.socketio_app import sio
from core.socket.user_sessions import get_user_session_namespace

app = create_app()
logger = logging.getLogger("app")
socketio_app = ASGIApp(sio, static_files={"/static/": settings.STATIC_ROOT})

user_session_namespace = get_user_session_namespace()
sio.register_namespace(user_session_namespace)

app.mount("/socket.io", socketio_app)


if __name__ == "__main__":
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION} env={settings.ENVIRONMENT} debug={settings.DEBUG}")
    uvicorn.run(
        "run:app",
        host="127.0.0.1",
        port=settings.PORT,
        reload=settings.DEBUG
    )
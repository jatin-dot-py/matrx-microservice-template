
import logging
from dotenv import load_dotenv
from socketio import ASGIApp
from core import settings
from matrx_utils import vcprint

from matrx_utils.core.sio_app import sio

# Initialize database models
vcprint("---- Initializing Database Models ----", color="bright_teal")
import core.scripts.initialize_db_models
vcprint("---- Initializing Database Models finished ----", color="bright_teal")


vcprint("---- Initializing Service Factory ----", color="bright_teal")
import core.socket.core.app_factory
vcprint("---- Initialized Service Factory finished ----", color="bright_teal")


from matrx_utils.socket.core.user_sessions import get_user_session_namespace
from app.api import create_app

# Load environment variables and configure logger
load_dotenv()
import core.system_logger
vcprint("[APP.py] Loaded environment variables", color="green")
vcprint("[APP.py] Configured Settings", color="green")


# Create FastAPI app
app = create_app()
vcprint("[APP.py] Created Fast API app", color="green")

# Configure Socket.IO
logger = logging.getLogger("app")
socketio_app = ASGIApp(sio, static_files={"/static/": settings.STATIC_ROOT})
vcprint("[APP.py] Started socket app", color="green")
user_session_namespace = get_user_session_namespace()
sio.register_namespace(user_session_namespace)
app.mount("/socket.io", socketio_app)

# The `app` object is now defined at the module level for Uvicorn to import

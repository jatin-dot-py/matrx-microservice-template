import socketio

# Initialize Socket.IO server
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*",
)

clients = {}
verbose = True

from core.socket.initialize_handlers import initialize_socketio_handlers

initialize_socketio_handlers()

from matrx_utils.socket.core.service_factory import ServiceFactory
from core.socketio_app import sio
from core.socket.services.log_service import LogService


class AppServiceFactory(ServiceFactory):
    def __init__(self):
        super().__init__()
        self.add_sio_instance(sio_instance=sio)


        # Register YOUR app's services using the inherited methods
        self.register_service("log_service", LogService)
        # self.register_multi_instance_service...